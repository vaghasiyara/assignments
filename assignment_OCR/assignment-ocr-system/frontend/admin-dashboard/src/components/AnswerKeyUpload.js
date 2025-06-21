import React, { useState } from 'react';
import axios from 'axios';

const AnswerKeyUpload = () => {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState('');

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append('file', file);
    try {
      const res = await axios.post('http://127.0.0.1:8003/upload-answer-sheet', formData);
      setMessage(res.data.message);
    } catch (err) {
      setMessage('Error uploading file');
    }
  };

  return (
    <div>
      <h2>Upload Answer Sheet</h2>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload}>Upload</button>
      <p>{message}</p>
    </div>
  );
};

export default AnswerKeyUpload;
