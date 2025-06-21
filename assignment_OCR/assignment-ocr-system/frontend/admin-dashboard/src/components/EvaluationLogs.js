import React, { useEffect, useState } from 'react';
import axios from 'axios';

const EvaluationLogs = () => {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8003/logs')
      .then(response => {
        setLogs(response.data.logs);
      })
      .catch(error => {
        console.error('Error fetching logs:', error);
      });
  }, []);

  return (
    <div>
      <h2>Evaluation Logs</h2>
      <table border="1" cellPadding="5" style={{ borderCollapse: 'collapse', width: '100%' }}>
        <thead>
          <tr>
            <th>Student</th>
            <th>Filename</th>
            <th>Score</th>
            <th>Late?</th>
            <th>Date</th>
          </tr>
        </thead>
        <tbody>
          {logs.map((log, index) => (
            <tr key={index}>
              <td>{log.student || 'N/A'}</td>
              <td>{log.filename}</td>
              <td>{log.score}</td>
              <td>{log.late ? 'Yes' : 'No'}</td>
              <td>{log.timestamp || 'N/A'}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default EvaluationLogs;
