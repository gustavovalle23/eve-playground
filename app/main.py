import os
from eve import Eve
from eve_swagger import get_swagger_blueprint
from app.auth.auth import hash_passwords

SETTINGS_PATH = os.path.join(os.path.dirname(__file__), "settings.py")
app = Eve(settings=SETTINGS_PATH)

app.on_insert_users += hash_passwords

app.register_blueprint(get_swagger_blueprint())
app.config['SWAGGER_INFO'] = {
    'title': 'Eve Playground API',
    'version': '1.0',
    'description': 'Pydantic + Cerberus Eve API',
    'contact': {
        'name': 'Gustavo Valle',
        'email': 'gustavo@devcrafter.io'
    }
}

if __name__ == "__main__":
    app.run(debug=os.getenv("DEBUG") == "True")
