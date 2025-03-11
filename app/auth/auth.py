import secrets
from bcrypt import gensalt, hashpw
from eve.auth import TokenAuth
from flask import g

class RoleBasedTokenAuth(TokenAuth):
    def check_auth(self, token, allowed_roles, resource, method):
        user = self.app.data.driver.db["users"].find_one({"token": token})

        if user:
            g.current_user = user
            if allowed_roles and user.get("role") not in allowed_roles:
                return False
            return True
        return False


def hash_passwords(items):
    for item in items:
        if "password" in item:
            item["password"] = hashpw(item["password"].encode(), gensalt()).decode()

        if "token" not in item:
            item["token"] = secrets.token_hex(32)
