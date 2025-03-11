import os
from dotenv import load_dotenv
from app.auth.auth import RoleBasedTokenAuth

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DBNAME = os.getenv("MONGO_DBNAME")
DEBUG = os.getenv("DEBUG") == "True"

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']

from app.schemas.user import users

DOMAIN = {
    'users': {
        **users,
        "resource_methods": ["GET", "POST"],
        "item_methods": ["GET", "PATCH", "DELETE"],
        "authentication": RoleBasedTokenAuth,
        "allowed_roles": ["admin"],
    }
}
