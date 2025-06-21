import React, { useState } from 'react';
import axios from 'axios';

const AssignmentUpload = () => {
  const [file, setFile] = useState(null);
  const [student, setStudent] = useState('');
  const [message, setMessage] = useState('');

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append('file', file);
    formData.append('student', student);

    try {
      const res = await axios.post('http://127.0.0.1:8003/upload-assignment', formData);
      setMessage(`Score: ${res.data.score} | Late: ${res.data.late ? "Yes" : "No"}`);
    } catch (err) {
      setMessage('Error uploading assignment');
    }
  };

  return (
    <div>
      <h2>Upload Assignment</h2>
      <input
        type="text"
        placeholder="Student Name"
        value={student}
        onChange={(e) => setStudent(e.target.value)}
      />
      <br />
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <br />
      <button onClick={handleUpload}>Upload</button>
      <p>{message}</p>
    </div>
  );
};

export default AssignmentUpload;
