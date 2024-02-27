from flask import Flask, jsonify
from auth_db.generate_token import generate_token
from auth_db.token_required import  token_required

app = Flask(__name__)


@app.route('/generate_token', methods=['POST'])
def get_token():
    return generate_token()

@app.route('/protected_route', methods=['GET'])
@token_required
def protected_route():
    return jsonify({'message': 'This is a protected route!'})

if __name__ == '__main__':
    app.run(debug=True)
