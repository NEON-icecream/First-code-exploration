import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [analysis, setAnalysis] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/analysis')
      .then(response => response.json())
      .then(data => setAnalysis(data))
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  if (!analysis) {
    return (
      <div className="App">
        <header className="App-header">
          <h1>Student Performance Pattern Analyzer</h1>
          <p>Loading analysis...</p>
        </header>
      </div>
    );
  }

  return (
    <div className="App">
      <header className="App-header">
        <h1>Student Performance Pattern Analyzer</h1>
        <p>Software Systems Capstone — CPSC 49200</p>
        <p>Built with React | Powered by Python and NumPy</p>
        <p>By: Mahshid D. Alam</p>

        <h2>Class Ranking</h2>
        <table style={{ color: 'white', margin: '0 auto', borderSpacing: '20px 5px' }}>
          <thead>
            <tr>
              <th>Rank</th>
              <th>Student</th>
              <th>Average</th>
              <th>GPA</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {analysis.ranking.map((s, i) => (
              <tr key={i}>
                <td>{s.rank}</td>
                <td>{s.student}</td>
                <td>{s.average}</td>
                <td>{s.gpa}</td>
                <td>{s.status}</td>
              </tr>
            ))}
          </tbody>
        </table>

        <h2>Subject Averages</h2>
        <ul>
          {analysis.subjects.map((subj, i) => (
            <li key={i}>{subj.subject}: {subj.average}</li>
          ))}
        </ul>
        <p>Strongest: {analysis.strongest_subject} | Weakest: {analysis.weakest_subject}</p>

        <h2>Eigenvalue Analysis</h2>
        <p>Dominant Pattern: Pattern {analysis.dominant_pattern}</p>
        <p>Eigenvalues: {analysis.eigenvalues.join(', ')}</p>

        <h2>Bias Awareness Note</h2>
        <p style={{ maxWidth: '600px', fontSize: '16px' }}>{analysis.bias_note}</p>
      </header>
    </div>
  );
}

export default App;