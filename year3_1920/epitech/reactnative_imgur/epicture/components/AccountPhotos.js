import React, { Component } from 'react';
import { View, Button, SafeAreaView, Text } from 'react-native';

import PhotoList from '../utilities/Photos';
import { secureGet } from '../utilities/SecureStorage';
import { imgur_account_my_images } from '../api/Constants';


export default class AccountPhotos extends Component {

  constructor(props) {
    super(props);
    this.state = {
      dataSource: null,
    }
  }

  async componentDidMount() {
    console.log("Downloading my account images");
    let dataSource = await getAccountImages();
    this.setState(previousState => ({ dataSource: dataSource}));
  }

  render() {
    if ( this.state.dataSource ) {
      return (
        <PhotoList dataSource={ this.state.dataSource } />
     );
    } else {
      return null;
    }
  }
}


async function getAccountImages() {
  try {
    let accessToken = await secureGet('accessToken');
    let response = await fetch(imgur_account_my_images, {
      headers: {
        'Authorization': 'Bearer ' + accessToken
      }
    });
    let responseJson = await response.json();
    console.log(response);
    return responseJson;
  } catch (error) {
    console.error(error);
  }
}
