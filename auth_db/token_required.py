from functools import wraps
from flask import jsonify, request
import jwt
import traceback
from auth_db.client_info import get_client_info

def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        try:
            token = request.headers.get('Authorization')
            if token and token.startswith('Bearer '):
                token = token.split('Bearer ')[1]
            client_id = request.form.get('client_id')
            if not client_id:
                return jsonify({'Alert!': 'Client ID is Missing'})
            if not token:
                return jsonify({'Alert!': 'Token is missing!'})

            client_info = get_client_info(client_id)

            if client_id != client_info.get("client_id"):
                return jsonify({'Alert!': 'Invalid Client ID'})
            secret_key = client_info.get("client_secret_key")

            data = jwt.decode(token, secret_key, algorithms=["HS256"])
            if not data:
                return jsonify({'Alert!': 'Invalid Token'})
            return func(*args, **kwargs)
        except Exception as e:
            traceback.print_exc()
            return jsonify({'Alert!': 'Invalid Token'})
    return decorated
