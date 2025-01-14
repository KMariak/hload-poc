const awsconfig = {
  Auth: {
    mandatorySignIn: true,
    region: 'us-east-1',
    userPoolId: 'us-east-1_my-user-pool-id',
    userPoolWebClientId: 'my-app-client-id', //
    authenticationFlowType: 'USER_PASSWORD_AUTH',
    endpoint: 'http://localhost:4566'
  }
};

export default awsconfig;