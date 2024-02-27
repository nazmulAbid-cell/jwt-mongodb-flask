from auth_db.client_info import get_client_info
import jwt
from datetime import datetime, timedelta
from flask import Flask, jsonify, request

def generate_token():
    try:
        client_id = request.form.get("client_id")
        client_info = get_client_info(client_id)
        print(client_info)
        client_secret_key = request.form.get("client_secret_key")

        if client_info is None or client_info.get("client_secret_key") != client_secret_key:
            return None

        # Generate JWT token
        payload = {
            'client_id': client_id,
            'exp': datetime.utcnow() + timedelta(minutes=30)  # Token expires in 30 minutes
        }
        token = jwt.encode(payload, client_secret_key, algorithm='HS256')
        print(token)

        return jsonify({"responseCode": 200, "message": "Token generated successfully", "token": token})
    except Exception as e:
        return jsonify({"Error": str(e)})