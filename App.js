import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [students, setStudents] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/students')
      .then(response => response.json())
      .then(data => setStudents(data))
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Student Performance Pattern Analyzer</h1>
        <p>Software Systems Capstone — CPSC 49200</p>
        <p>Built with React | Powered by Python and NumPy</p>
        <p>By: Mahshid D. Alam</p>

        <h2>Student Data (from Flask API)</h2>
        <ul>
          {students.map((student, index) => (
            <li key={index}>{student.name} — GPA: {student.gpa}</li>
          ))}
        </ul>
      </header>
    </div>
  );
}

export default App;