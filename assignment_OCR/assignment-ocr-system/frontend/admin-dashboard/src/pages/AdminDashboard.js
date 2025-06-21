import React from 'react';
import AnswerKeyUpload from '../components/AnswerKeyUpload';
import EvaluationLogs from '../components/EvaluationLogs';

const AdminDashboard = () => {
  return (
    <div>
      <h1>Admin Dashboard</h1>
      <AnswerKeyUpload />
      <hr />
      <EvaluationLogs />
    </div>
  );
};

export default AdminDashboard;
