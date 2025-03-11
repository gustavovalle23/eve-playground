from eve.auth import TokenAuth
from werkzeug.security import check_password_hash
from flask import g

MOCK_USERS = {
    "admin-token": {"username": "admin", "role": "admin"},
    "user-token": {"username": "john", "role": "user"},
}

class RoleBasedTokenAuth(TokenAuth):
    def check_auth(self, token, allowed_roles, resource, method):
        user = MOCK_USERS.get(token)
        if user:
            g.current_user = user
            if allowed_roles and user["role"] not in allowed_roles:
                return False
            return True
        return False
