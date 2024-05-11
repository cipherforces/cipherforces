import hashlib
import bcrypt
from flask import Flask, render_template, redirect, url_for, request, flash, jsonify, send_from_directory
from pymongo import MongoClient
from flask_cors import CORS, cross_origin
import os
root = os.path.join(os.path.dirname(os.path.abspath(__file__)))
client = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB URI if needed
db = client['cipherforces']
users = db['users']  # Collection to store user data

app = Flask(__name__)
CORS(app)
app.secret_key = '0144436102'  # Set a strong secret key

def hash_username(username):
    return hashlib.sha256(username.encode()).hexdigest()

def hash_password_SHA(username):
    return hashlib.sha256(username.encode()).hexdigest()


def hash_password(password,salt):
    return bcrypt.hashpw(password.encode(), salt)

def hash_with_salt(value, salt):
    return hashlib.sha256((value + salt).encode()).hexdigest()

@app.route('/register', methods=['GET', 'POST'])
@cross_origin(origins=["*"])  # Allow requests from this origin
def register():
    response = jsonify({"data": "Some data"})
    response.headers['Access-Control-Allow-Origin'] = '*'
    if request.method == 'POST':
        data = request.get_json()
        email = data['email']
        password = data['password']

        email = hash_username(email)
        #salt = hash_password_SHA(password)
        #password = hash_with_salt(password,salt)
        password = hash_password_SHA(password)
        # Input validation and error handling (essential for security)
        existing_user = users.find_one({'email': email})
        if existing_user:
            flash('Username already exists.')
            return 'Exists'
        else:
            users.insert_one({'email': email, 'password': password})
            flash('Registration successful!')
        #return redirect('F:\MEC\Encryption\cipherforces\index.html')
        return 'done'   
    else:
        return render_template('register.html')
@app.route('/<path:path>', methods=['GET'])
def static_proxy(path):
    return send_from_directory(root, path)
@app.route("/registerfile", methods=['GET', 'POST'])
def registerfile():
  """Renders the register.html template"""
  return send_from_directory(root, 'Register.html')
CORS(app)  # Apply CORS globally to all routes
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
################################################################33
    
@app.route('/login', methods=['POST'])
@cross_origin(origins=["*"])  # Allow requests from this origin
def login():
    response = jsonify({"data": "Some data"})
    response.headers['Access-Control-Allow-Origin'] = '*'
    data = request.get_json()
    email = data['email']
    password = data['password']
    
    email = hash_username(email)
    
    # Query MongoDB to find the user by username
    user = users.find_one({'email': email})
    #password = hash_password_SHA(password)
    if user:
        # Login successful, redirect to index page
        return redirect(url_for('index'))
        #return 'done'
    else:
        # Invalid username or password, stay on login page
        return render_template('login.html', message='Invalid username or password')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/<path:path>', methods=['GET'])
def static_proxy(path):
    return send_from_directory(root, path)
@app.route("/loginfile", methods=['GET', 'POST'])
def loginfile():
  """Renders the register.html template"""
  return send_from_directory(root, 'login.html')
CORS(app)  # Apply CORS globally to all routes
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')