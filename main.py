import os
import sys
# DON'T CHANGE THIS !!!
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, send_from_directory
from flask_cors import CORS
from src.models.user import db, User, Service, Order, Transaction, Provider
from src.routes.user import user_bp
from src.routes.auth import auth_bp
from src.routes.services import services_bp
from src.routes.orders import orders_bp
from src.routes.wallet import wallet_bp

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))
app.config['SECRET_KEY'] = 'asdf#FGSgvasgf$5$WGT'

# Enable CORS for all routes
CORS(app, supports_credentials=True)

# Register blueprints
app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(services_bp, url_prefix='/api')
app.register_blueprint(orders_bp, url_prefix='/api')
app.register_blueprint(wallet_bp, url_prefix='/api')

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'database', 'app.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def init_sample_data():
    """Initialize sample data for testing"""
    # Check if services already exist
    if Service.query.first():
        return
    
    # Create sample services
    services_data = [
        # Instagram Services
        {
            'name': 'متابعين انستقرام - جودة عالية',
            'description': 'متابعين حقيقيين ونشطين لحسابك على انستقرام',
            'platform': 'instagram',
            'service_type': 'followers',
            'price_per_1000': 5.0,
            'min_quantity': 100,
            'max_quantity': 50000
        },
        {
            'name': 'لايكات انستقرام - سريعة',
            'description': 'لايكات سريعة وآمنة لمنشوراتك',
            'platform': 'instagram',
            'service_type': 'likes',
            'price_per_1000': 2.0,
            'min_quantity': 50,
            'max_quantity': 10000
        },
        {
            'name': 'مشاهدات انستقرام - ريلز',
            'description': 'مشاهدات عالية الجودة لفيديوهات الريلز',
            'platform': 'instagram',
            'service_type': 'views',
            'price_per_1000': 1.0,
            'min_quantity': 100,
            'max_quantity': 100000
        },
        
        # TikTok Services
        {
            'name': 'متابعين تيك توك - نشطين',
            'description': 'متابعين حقيقيين ومتفاعلين لحسابك على تيك توك',
            'platform': 'tiktok',
            'service_type': 'followers',
            'price_per_1000': 4.0,
            'min_quantity': 100,
            'max_quantity': 30000
        },
        {
            'name': 'لايكات تيك توك - سريعة',
            'description': 'لايكات سريعة التنفيذ لفيديوهاتك',
            'platform': 'tiktok',
            'service_type': 'likes',
            'price_per_1000': 1.5,
            'min_quantity': 50,
            'max_quantity': 20000
        },
        {
            'name': 'مشاهدات تيك توك - عالية الجودة',
            'description': 'مشاهدات حقيقية ومضمونة',
            'platform': 'tiktok',
            'service_type': 'views',
            'price_per_1000': 0.5,
            'min_quantity': 1000,
            'max_quantity': 1000000
        },
        
        # YouTube Services
        {
            'name': 'مشتركين يوتيوب - حقيقيين',
            'description': 'مشتركين حقيقيين ومهتمين بمحتواك',
            'platform': 'youtube',
            'service_type': 'subscribers',
            'price_per_1000': 8.0,
            'min_quantity': 50,
            'max_quantity': 10000
        },
        {
            'name': 'لايكات يوتيوب - طبيعية',
            'description': 'لايكات طبيعية ومتدرجة لفيديوهاتك',
            'platform': 'youtube',
            'service_type': 'likes',
            'price_per_1000': 3.0,
            'min_quantity': 50,
            'max_quantity': 5000
        },
        {
            'name': 'مشاهدات يوتيوب - احتفاظ عالي',
            'description': 'مشاهدات عالية الاحتفاظ لتحسين ترتيب الفيديو',
            'platform': 'youtube',
            'service_type': 'views',
            'price_per_1000': 2.0,
            'min_quantity': 100,
            'max_quantity': 100000
        },
        
        # Twitter Services
        {
            'name': 'متابعين تويتر - نشطين',
            'description': 'متابعين نشطين ومتنوعين لحسابك',
            'platform': 'twitter',
            'service_type': 'followers',
            'price_per_1000': 6.0,
            'min_quantity': 100,
            'max_quantity': 20000
        },
        {
            'name': 'لايكات تويتر - سريعة',
            'description': 'لايكات سريعة وآمنة لتغريداتك',
            'platform': 'twitter',
            'service_type': 'likes',
            'price_per_1000': 2.5,
            'min_quantity': 50,
            'max_quantity': 10000
        },
        {
            'name': 'ريتويت - طبيعي',
            'description': 'إعادة تغريد طبيعية لزيادة الانتشار',
            'platform': 'twitter',
            'service_type': 'retweets',
            'price_per_1000': 3.0,
            'min_quantity': 25,
            'max_quantity': 5000
        }
    ]
    
    for service_data in services_data:
        service = Service(**service_data)
        db.session.add(service)
    
    db.session.commit()
    print("Sample services created successfully!")

with app.app_context():
    db.create_all()
    init_sample_data()

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    static_folder_path = app.static_folder
    if static_folder_path is None:
            return "Static folder not configured", 404

    if path != "" and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)
    else:
        index_path = os.path.join(static_folder_path, 'index.html')
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, 'index.html')
        else:
            return "index.html not found", 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
