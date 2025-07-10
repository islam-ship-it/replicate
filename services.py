from flask import Blueprint, request, jsonify
from src.models.user import db, Service

services_bp = Blueprint('services', __name__)

@services_bp.route('/services', methods=['GET'])
def get_services():
    try:
        # Get query parameters
        platform = request.args.get('platform')
        service_type = request.args.get('type')
        status = request.args.get('status', 'active')
        
        # Build query
        query = Service.query.filter_by(status=status)
        
        if platform:
            query = query.filter_by(platform=platform)
        
        if service_type:
            query = query.filter_by(service_type=service_type)
        
        services = query.all()
        
        return jsonify({
            'services': [service.to_dict() for service in services],
            'total': len(services)
        }), 200
        
    except Exception as e:
        return jsonify({'error': 'Failed to fetch services'}), 500

@services_bp.route('/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    try:
        service = Service.query.get(service_id)
        
        if not service:
            return jsonify({'error': 'Service not found'}), 404
        
        if service.status != 'active':
            return jsonify({'error': 'Service is not available'}), 404
        
        return jsonify({'service': service.to_dict()}), 200
        
    except Exception as e:
        return jsonify({'error': 'Failed to fetch service'}), 500

@services_bp.route('/services/platforms', methods=['GET'])
def get_platforms():
    try:
        platforms = db.session.query(Service.platform).filter_by(status='active').distinct().all()
        platform_list = [platform[0] for platform in platforms]
        
        return jsonify({'platforms': platform_list}), 200
        
    except Exception as e:
        return jsonify({'error': 'Failed to fetch platforms'}), 500

@services_bp.route('/services/types', methods=['GET'])
def get_service_types():
    try:
        platform = request.args.get('platform')
        
        query = db.session.query(Service.service_type).filter_by(status='active')
        
        if platform:
            query = query.filter_by(platform=platform)
        
        types = query.distinct().all()
        type_list = [service_type[0] for service_type in types]
        
        return jsonify({'types': type_list}), 200
        
    except Exception as e:
        return jsonify({'error': 'Failed to fetch service types'}), 500

# Admin routes for managing services (would require admin authentication in production)
@services_bp.route('/admin/services', methods=['POST'])
def create_service():
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['name', 'platform', 'service_type', 'price_per_1000']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'error': f'{field} is required'}), 400
        
        service = Service(
            name=data['name'],
            description=data.get('description', ''),
            platform=data['platform'],
            service_type=data['service_type'],
            price_per_1000=float(data['price_per_1000']),
            min_quantity=int(data.get('min_quantity', 100)),
            max_quantity=int(data.get('max_quantity', 100000)),
            provider_id=data.get('provider_id')
        )
        
        db.session.add(service)
        db.session.commit()
        
        return jsonify({
            'message': 'Service created successfully',
            'service': service.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to create service'}), 500

@services_bp.route('/admin/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    try:
        service = Service.query.get(service_id)
        
        if not service:
            return jsonify({'error': 'Service not found'}), 404
        
        data = request.get_json()
        
        # Update fields if provided
        if 'name' in data:
            service.name = data['name']
        if 'description' in data:
            service.description = data['description']
        if 'platform' in data:
            service.platform = data['platform']
        if 'service_type' in data:
            service.service_type = data['service_type']
        if 'price_per_1000' in data:
            service.price_per_1000 = float(data['price_per_1000'])
        if 'min_quantity' in data:
            service.min_quantity = int(data['min_quantity'])
        if 'max_quantity' in data:
            service.max_quantity = int(data['max_quantity'])
        if 'status' in data:
            service.status = data['status']
        if 'provider_id' in data:
            service.provider_id = data['provider_id']
        
        db.session.commit()
        
        return jsonify({
            'message': 'Service updated successfully',
            'service': service.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to update service'}), 500

@services_bp.route('/admin/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    try:
        service = Service.query.get(service_id)
        
        if not service:
            return jsonify({'error': 'Service not found'}), 404
        
        # Soft delete by setting status to inactive
        service.status = 'inactive'
        db.session.commit()
        
        return jsonify({'message': 'Service deleted successfully'}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to delete service'}), 500

