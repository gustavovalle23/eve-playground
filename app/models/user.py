from pymongo import IndexModel, ASCENDING

user_schema = {
    'username': {'type': 'string', 'unique': True, 'minlength': 3, 'maxlength': 50},
    'email': {'type': 'string', 'unique': True},
    'age': {'type': 'integer', 'min': 18}
}

users = {
    'schema': user_schema,
    'resource_methods': ['GET', 'POST', 'DELETE'],
    'item_methods': ['GET', 'PATCH', 'DELETE'],
    'indexes': [IndexModel([("username", ASCENDING)], unique=True)]
}
