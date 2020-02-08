import React, { Component } from 'react';
import { WebView } from 'react-native-webview';
const urlParse = require('url-parse');
const queryString = require('query-string');

import { imgur_auth_uri, auth_callback_uri } from '../api/Constants';
import { clientId } from '../Config';
import { secureSet } from '../utilities/SecureStorage';


export default class Login extends Component {

  constructor(props) {
    super(props);
    this.webview = null;
  }

  render() {
    let url = urlParse(imgur_auth_uri, true);
    state = 'login';
    url.set('query', {
        client_id: clientId,
        response_type: 'token',
        state: state,
    });
    auth_uri = url.toString();
    console.log("going to: " + auth_uri);
    return (
      <WebView
        ref={ref => (this.webview = ref)} // make the created component accessible from outside
        source={{ uri: auth_uri }}
        style={{ marginTop: 20 }}
        cacheEnabled={ false }
        incognito={ true }
        onNavigationStateChange={ this.handleLoginNavigationChange }
      />
    );
  }

  handleLoginNavigationChange = navState => {
    const url = urlParse(navState.url, false);
    console.log("navigation change to");
    console.log(url);

    if (!url.href.startsWith(imgur_auth_uri)) {
      // left the log in page
      this.props.callback(false, false);
      this.webview.stopLoading();

      if (url.href.startsWith(auth_callback_uri)) {
        // went to callback page
        if (url.hash.includes("access_token")) {
          // successful login
          let { state } = queryString.parse(url.query);
          let { access_token, expires_in, token_type, refresh_token, account_username, account_id } = queryString.parse(url.hash);

          secureSet('accessToken', access_token);
          secureSet('expiresIn', expires_in);
          secureSet('tokenType', token_type);
          secureSet('refreshToken', refresh_token); 
          secureSet('accountUsername', account_username);
          secureSet('accountId', account_id);
          this.props.callback(false, true);
        } else if (url.query.includes('error=access_denied')) {
          // denied
          console.log("denied");
        }
      } else {
        // authentication unknown
        console.log("somewhere else");
      }
    }
  }
}
