from functools import wraps
from flask import request, jsonify

TOKEN = "mysecrettoken"

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token or token != f"Bearer {TOKEN}":
            return jsonify({"message": "Token is missing or invalid!"}), 403
        return f(*args, **kwargs)
    return decorated