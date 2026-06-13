from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allows React (different port) to talk to this API

@app.route("/api/students")
def get_students():
    # Sample data for now - we'll connect bias_analyzer.py logic next
    students = [
        {"name": "Student A", "gpa": 3.5},
        {"name": "Student B", "gpa": 2.8},
        {"name": "Student C", "gpa": 3.9}
    ]
    return jsonify(students)

if __name__ == "__main__":
    app.run(debug=True, port=5000)