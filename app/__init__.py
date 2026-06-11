from flask import Flask

# Create the Flask application
def create_app():
    app = Flask(__name__) 
    
    from .routes import main
    app.register_blueprint(main)

    return app
