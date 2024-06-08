from flask import Flask

def create_app():
    '''
    Configures and creates the Flask application,

    Inputs:
        None

    Outputs:
        app(Flask)
    '''
    app = Flask(__name__)
    app.secret_key = 'secret'

    from views import app_routes
    app.register_blueprint(app_routes)

    return app