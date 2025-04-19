import os
import hashlib
import logging
from flask import Flask, request

# 1. Hardcoded Credentials
USERNAME = "admin"
PASSWORD = "SuperSecret123"

# 2. Insecure Dependency (MD5 for password hashing)
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

# 3. Inadequate Logging Practices (Logging sensitive information)
logging.basicConfig(level=logging.DEBUG)
logging.debug(f"Admin credentials: {USERNAME}/{PASSWORD}")

# 4. Flask App with Missing Security Headers
app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # 5. Lack of Input Validation
    username = request.form['username']
    password = request.form['password']
    
    # 6. Improper Error Handling (Detailed error messages)
    try:
        if username == USERNAME and password == PASSWORD:
            return "Access granted"
        else:
            return "Access denied"
    except Exception as e:
        return f"An error occurred: {e}"

@app.route('/execute', methods=['POST'])
def execute():
    # 7. Command Injection Vulnerability
    command = request.form['command']
    os.system(command)
    return "Command executed"

@app.route('/delete_user', methods=['POST'])
def delete_user():
    # 8. Insufficient Access Controls (No authentication/authorization checks)
    user_id = request.form['user_id']
    # Code to delete user without verifying permissions
    return f"User {user_id} deleted."

@app.route('/upload', methods=['POST'])
def upload():
    # 9. Path Traversal Vulnerability
    file = request.files['file']
    file.save(f"/uploads/{file.filename}")
    return "File uploaded"

@app.route('/data', methods=['GET'])
def data():
    # 10. Verbose Error Messages (Potentially revealing stack traces)
    raise Exception("This is a test exception to demonstrate verbose error messages.")

if __name__ == '__main__':
    app.run(debug=True)
