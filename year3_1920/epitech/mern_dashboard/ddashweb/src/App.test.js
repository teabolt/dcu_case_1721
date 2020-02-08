import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';


// let SERVER_URI = `http://${process.env.SERVER_HOST}:${process.env.SERVER_PORT}`


it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<App />, div);
  ReactDOM.unmountComponentAtNode(div);
});


// it('connects to server', () => {
//   expect.assertions(1);
//   fetch(SERVER_URI + '/api/ping')
//     .then(res => res.text())
//     .then(res => expect(res).toEqual('pong'));
// });