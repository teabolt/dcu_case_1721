import React, { Component } from 'react';

import { secureDel } from '../utilities/SecureStorage';


export default class Logout extends Component {

  async componentDidMount() {
    await secureDel('accessToken');
    await secureDel('expiresIn');
    await secureDel('tokenType');
    await secureDel('refreshToken'); 
    await secureDel('accountUsername');
    await secureDel('accountId');
    this.props.callback(false, false);
  }

  render() {
    return null;
  }
}
