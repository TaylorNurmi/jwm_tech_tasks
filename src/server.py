from __init__ import create_app
from views import app_routes

app = create_app()
app.register_blueprint(app_routes)

if __name__ == '__main__':
    app.run(debug=True)
