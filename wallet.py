from flask import Blueprint, request, jsonify, session
from src.models.user import db, User, Transaction

wallet_bp = Blueprint('wallet', __name__)

@wallet_bp.route('/wallet/balance', methods=['GET'])
def get_balance():
    if 'user_id' not in session:
        return jsonify({'error': 'Not authenticated'}), 401
    
    try:
        user = User.query.get(session['user_id'])
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        return jsonify({'balance': user.balance}), 200
        
    except Exception as e:
        return jsonify({'error': 'Failed to fetch balance'}), 500

@wallet_bp.route('/wallet/transactions', methods=['GET'])
def get_transactions():
    if 'user_id' not in session:
        return jsonify({'error': 'Not authenticated'}), 401
    
    try:
        user_id = session['user_id']
        
        # Get query parameters
        transaction_type = request.args.get('type')
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 20))
        
        # Build query
        query = Transaction.query.filter_by(user_id=user_id)
        
        if transaction_type:
            query = query.filter_by(type=transaction_type)
        
        # Order by creation date (newest first)
        query = query.order_by(Transaction.created_at.desc())
        
        # Paginate
        transactions = query.paginate(
            page=page, 
            per_page=per_page, 
            error_out=False
        )
        
        return jsonify({
            'transactions': [transaction.to_dict() for transaction in transactions.items],
            'total': transactions.total,
            'pages': transactions.pages,
            'current_page': page,
            'per_page': per_page
        }), 200
        
    except Exception as e:
        return jsonify({'error': 'Failed to fetch transactions'}), 500

@wallet_bp.route('/wallet/add-funds', methods=['POST'])
def add_funds():
    if 'user_id' not in session:
        return jsonify({'error': 'Not authenticated'}), 401
    
    try:
        user_id = session['user_id']
        data = request.get_json()
        
        # Validate required fields
        if not data.get('amount') or not data.get('payment_method'):
            return jsonify({'error': 'Amount and payment method are required'}), 400
        
        amount = float(data['amount'])
        payment_method = data['payment_method']
        
        # Validate amount
        if amount <= 0:
            return jsonify({'error': 'Amount must be greater than 0'}), 400
        
        if amount < 10:  # Minimum deposit
            return jsonify({'error': 'Minimum deposit amount is $10'}), 400
        
        if amount > 10000:  # Maximum deposit
            return jsonify({'error': 'Maximum deposit amount is $10,000'}), 400
        
        # Validate payment method
        valid_methods = ['credit_card', 'bank_transfer', 'paypal', 'crypto']
        if payment_method not in valid_methods:
            return jsonify({'error': 'Invalid payment method'}), 400
        
        # In a real application, you would integrate with a payment processor here
        # For now, we'll simulate a successful payment
        
        # Create pending transaction
        transaction = Transaction(
            user_id=user_id,
            type='deposit',
            amount=amount,
            description=f'Deposit via {payment_method}',
            status='pending',
            payment_method=payment_method
        )
        
        db.session.add(transaction)
        db.session.commit()
        
        # Simulate payment processing (in real app, this would be handled by webhook)
        # For demo purposes, we'll immediately mark as completed and add to balance
        transaction.status = 'completed'
        
        user = User.query.get(user_id)
        user.balance += amount
        
        db.session.commit()
        
        return jsonify({
            'message': 'Funds added successfully',
            'transaction': transaction.to_dict(),
            'new_balance': user.balance
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to add funds'}), 500

@wallet_bp.route('/wallet/payment-methods', methods=['GET'])
def get_payment_methods():
    """Get available payment methods"""
    payment_methods = [
        {
            'id': 'credit_card',
            'name': 'Credit/Debit Card',
            'description': 'Visa, Mastercard, American Express',
            'min_amount': 10,
            'max_amount': 10000,
            'processing_time': 'Instant',
            'fees': '2.9% + $0.30'
        },
        {
            'id': 'bank_transfer',
            'name': 'Bank Transfer',
            'description': 'Direct bank transfer',
            'min_amount': 50,
            'max_amount': 50000,
            'processing_time': '1-3 business days',
            'fees': 'Free'
        },
        {
            'id': 'paypal',
            'name': 'PayPal',
            'description': 'Pay with your PayPal account',
            'min_amount': 10,
            'max_amount': 10000,
            'processing_time': 'Instant',
            'fees': '3.4% + $0.30'
        },
        {
            'id': 'crypto',
            'name': 'Cryptocurrency',
            'description': 'Bitcoin, Ethereum, USDT',
            'min_amount': 25,
            'max_amount': 25000,
            'processing_time': '10-60 minutes',
            'fees': '1%'
        }
    ]
    
    return jsonify({'payment_methods': payment_methods}), 200

@wallet_bp.route('/wallet/statistics', methods=['GET'])
def get_wallet_statistics():
    if 'user_id' not in session:
        return jsonify({'error': 'Not authenticated'}), 401
    
    try:
        user_id = session['user_id']
        
        # Get total deposits
        total_deposits = db.session.query(db.func.sum(Transaction.amount)).filter_by(
            user_id=user_id, 
            type='deposit', 
            status='completed'
        ).scalar() or 0
        
        # Get total spent on orders
        total_spent = db.session.query(db.func.sum(Transaction.amount)).filter_by(
            user_id=user_id, 
            type='order', 
            status='completed'
        ).scalar() or 0
        total_spent = abs(total_spent)  # Convert to positive number
        
        # Get total refunds
        total_refunds = db.session.query(db.func.sum(Transaction.amount)).filter_by(
            user_id=user_id, 
            type='refund', 
            status='completed'
        ).scalar() or 0
        
        # Get current balance
        user = User.query.get(user_id)
        current_balance = user.balance
        
        # Get transaction counts
        deposit_count = Transaction.query.filter_by(
            user_id=user_id, 
            type='deposit', 
            status='completed'
        ).count()
        
        order_count = Transaction.query.filter_by(
            user_id=user_id, 
            type='order', 
            status='completed'
        ).count()
        
        return jsonify({
            'current_balance': current_balance,
            'total_deposits': total_deposits,
            'total_spent': total_spent,
            'total_refunds': total_refunds,
            'deposit_count': deposit_count,
            'order_count': order_count
        }), 200
        
    except Exception as e:
        return jsonify({'error': 'Failed to fetch wallet statistics'}), 500

