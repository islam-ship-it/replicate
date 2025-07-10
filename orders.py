from flask import Blueprint, request, jsonify, session
from src.models.user import db, User, Service, Order, Transaction
import re

orders_bp = Blueprint('orders', __name__)

def validate_url(url):
    """Validate if the URL is a valid social media URL"""
    patterns = {
        'instagram': r'https?://(www\.)?instagram\.com/',
        'tiktok': r'https?://(www\.)?tiktok\.com/',
        'youtube': r'https?://(www\.)?youtube\.com/',
        'twitter': r'https?://(www\.)?twitter\.com/',
        'facebook': r'https?://(www\.)?facebook\.com/'
    }
    
    for platform, pattern in patterns.items():
        if re.match(pattern, url, re.IGNORECASE):
            return True
    
    return False

@orders_bp.route('/orders', methods=['GET'])
def get_orders():
    if 'user_id' not in session:
        return jsonify({'error': 'Not authenticated'}), 401
    
    try:
        user_id = session['user_id']
        
        # Get query parameters
        status = request.args.get('status')
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        
        # Build query
        query = Order.query.filter_by(user_id=user_id)
        
        if status:
            query = query.filter_by(status=status)
        
        # Order by creation date (newest first)
        query = query.order_by(Order.created_at.desc())
        
        # Paginate
        orders = query.paginate(
            page=page, 
            per_page=per_page, 
            error_out=False
        )
        
        return jsonify({
            'orders': [order.to_dict() for order in orders.items],
            'total': orders.total,
            'pages': orders.pages,
            'current_page': page,
            'per_page': per_page
        }), 200
        
    except Exception as e:
        return jsonify({'error': 'Failed to fetch orders'}), 500

@orders_bp.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    if 'user_id' not in session:
        return jsonify({'error': 'Not authenticated'}), 401
    
    try:
        user_id = session['user_id']
        order = Order.query.filter_by(id=order_id, user_id=user_id).first()
        
        if not order:
            return jsonify({'error': 'Order not found'}), 404
        
        return jsonify({'order': order.to_dict()}), 200
        
    except Exception as e:
        return jsonify({'error': 'Failed to fetch order'}), 500

@orders_bp.route('/orders', methods=['POST'])
def create_order():
    if 'user_id' not in session:
        return jsonify({'error': 'Not authenticated'}), 401
    
    try:
        user_id = session['user_id']
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['service_id', 'link', 'quantity']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'error': f'{field} is required'}), 400
        
        service_id = int(data['service_id'])
        link = data['link'].strip()
        quantity = int(data['quantity'])
        
        # Validate URL
        if not validate_url(link):
            return jsonify({'error': 'Invalid social media URL'}), 400
        
        # Get service
        service = Service.query.get(service_id)
        if not service or service.status != 'active':
            return jsonify({'error': 'Service not found or not available'}), 404
        
        # Validate quantity
        if quantity < service.min_quantity:
            return jsonify({'error': f'Minimum quantity is {service.min_quantity}'}), 400
        
        if quantity > service.max_quantity:
            return jsonify({'error': f'Maximum quantity is {service.max_quantity}'}), 400
        
        # Calculate charge
        charge = (quantity / 1000) * service.price_per_1000
        
        # Get user and check balance
        user = User.query.get(user_id)
        if user.balance < charge:
            return jsonify({'error': 'Insufficient balance'}), 400
        
        # Create order
        order = Order(
            user_id=user_id,
            service_id=service_id,
            link=link,
            quantity=quantity,
            remains=quantity,
            charge=charge
        )
        
        # Deduct balance
        user.balance -= charge
        
        # Create transaction record
        transaction = Transaction(
            user_id=user_id,
            type='order',
            amount=-charge,
            description=f'Order #{order.id} - {service.name}',
            status='completed'
        )
        
        db.session.add(order)
        db.session.add(transaction)
        db.session.commit()
        
        return jsonify({
            'message': 'Order created successfully',
            'order': order.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to create order'}), 500

@orders_bp.route('/orders/<int:order_id>/cancel', methods=['PUT'])
def cancel_order(order_id):
    if 'user_id' not in session:
        return jsonify({'error': 'Not authenticated'}), 401
    
    try:
        user_id = session['user_id']
        order = Order.query.filter_by(id=order_id, user_id=user_id).first()
        
        if not order:
            return jsonify({'error': 'Order not found'}), 404
        
        if order.status not in ['pending', 'in_progress']:
            return jsonify({'error': 'Order cannot be cancelled'}), 400
        
        # Calculate refund amount based on remaining quantity
        refund_amount = (order.remains / order.quantity) * order.charge
        
        # Update order status
        order.status = 'cancelled'
        
        # Refund balance
        user = User.query.get(user_id)
        user.balance += refund_amount
        
        # Create refund transaction
        transaction = Transaction(
            user_id=user_id,
            type='refund',
            amount=refund_amount,
            description=f'Refund for cancelled order #{order.id}',
            status='completed'
        )
        
        db.session.add(transaction)
        db.session.commit()
        
        return jsonify({
            'message': 'Order cancelled successfully',
            'refund_amount': refund_amount,
            'order': order.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to cancel order'}), 500

@orders_bp.route('/orders/calculate', methods=['POST'])
def calculate_order():
    try:
        data = request.get_json()
        
        if not data.get('service_id') or not data.get('quantity'):
            return jsonify({'error': 'Service ID and quantity are required'}), 400
        
        service_id = int(data['service_id'])
        quantity = int(data['quantity'])
        
        service = Service.query.get(service_id)
        if not service or service.status != 'active':
            return jsonify({'error': 'Service not found or not available'}), 404
        
        if quantity < service.min_quantity or quantity > service.max_quantity:
            return jsonify({
                'error': f'Quantity must be between {service.min_quantity} and {service.max_quantity}'
            }), 400
        
        charge = (quantity / 1000) * service.price_per_1000
        
        return jsonify({
            'service': service.to_dict(),
            'quantity': quantity,
            'charge': round(charge, 2),
            'price_per_1000': service.price_per_1000
        }), 200
        
    except Exception as e:
        return jsonify({'error': 'Failed to calculate order'}), 500

