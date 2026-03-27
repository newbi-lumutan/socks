from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# User model - a simple placeholder
users = {}  # This could be a database instead

# Register a new user
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Username and password required'}), 400
    username = data['username']
    password = generate_password_hash(data['password'], method='sha256')
    users[username] = {'password': password}
    return jsonify({'message': 'User registered successfully'}), 201

# Login route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Username and password required'}), 400
    user = users.get(data['username'])
    if user and check_password_hash(user['password'], data['password']):
        token = jwt.encode({'username': data['username'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, app.config['SECRET_KEY'])
        return jsonify({'token': token}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

if __name__ == '__main__':
    app.run(debug=True)
