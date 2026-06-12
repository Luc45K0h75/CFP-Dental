from flask import Flask
from flask_mail import Mail
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
mail = Mail()

# Create the Flask application
def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.secret_key = os.getenv('SECRET_KEY', 'dev')
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')

    mail.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    @app.context_processor
    def inject_now():
        return {'now': datetime.utcnow()}

    return app