import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './index.css';

// Імпортуємо бібліотеку Amplify та конфігурацію
import { Amplify } from 'aws-amplify';
import awsExports from './aws-exports';

// Ініціалізуємо Amplify
Amplify.configure(awsExports);

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);