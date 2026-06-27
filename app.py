from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required
)
from bias_analyzer import get_analysis

app = Flask(__name__)
CORS(app)

# Secret key used to sign the JWT tokens
app.config["JWT_SECRET_KEY"] = "capstone-secret-key-change-later"
jwt = JWTManager(app)

# Login endpoint - issues a token if username/password are correct
@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username", None)
    password = data.get("password", None)

    # Simple hardcoded check for this version
    if username == "admin" and password == "password123":
        token = create_access_token(identity=username)
        return jsonify(access_token=token)
    return jsonify({"msg": "Wrong username or password"}), 401

# Old sample endpoint - kept for reference (no protection)
@app.route("/api/students")
def get_students():
    students = [
        {"name": "Student A", "gpa": 3.5},
        {"name": "Student B", "gpa": 2.8},
        {"name": "Student C", "gpa": 3.9}
    ]
    return jsonify(students)

# Protected endpoint - now requires a valid JWT token
@app.route("/api/analysis")
@jwt_required()
def get_analysis_data():
    return jsonify(get_analysis())

# Public endpoint - unprotected version for the frontend to read this week
# (React token handling will be added next week, then it can use the protected route)
@app.route("/api/analysis-public")
def get_analysis_public():
    return jsonify(get_analysis())

if __name__ == "__main__":
    app.run(debug=True, port=5000)