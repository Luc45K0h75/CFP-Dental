from flask import Flask
from datetime import datetime

# Create the Flask application
def create_app():
    app = Flask(__name__, instance_relative_config=True)

    from .routes import main
    app.register_blueprint(main)

    @app.context_processor
    def inject_now():
        return {'now': datetime.utcnow()}

    return app