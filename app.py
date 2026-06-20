from flask import Flask, jsonify
from flask_cors import CORS
from bias_analyzer import get_analysis

app = Flask(__name__)
CORS(app)  # allows React (different port) to talk to this API

# Old sample endpoint - kept for reference
@app.route("/api/students")
def get_students():
    students = [
        {"name": "Student A", "gpa": 3.5},
        {"name": "Student B", "gpa": 2.8},
        {"name": "Student C", "gpa": 3.9}
    ]
    return jsonify(students)

# New endpoint - serves real analysis from bias_analyzer.py
@app.route("/api/analysis")
def get_analysis_data():
    return jsonify(get_analysis())

if __name__ == "__main__":
    app.run(debug=True, port=5000)