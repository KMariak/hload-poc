import React from 'react';
import { withAuthenticator } from '@aws-amplify/ui-react';
import '@aws-amplify/ui-react/styles.css';

function App() {
  return (
    <div className="App">
      <h1>Welcome to HLoad</h1>
      <p>You are now authenticated!</p>
    </div>
  );
}

export default withAuthenticator(App);