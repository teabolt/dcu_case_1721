import React, { Component } from 'react';
import { View, Button, SafeAreaView, Text } from 'react-native';
import { createAppContainer } from "react-navigation"
import { createStackNavigator } from "react-navigation-stack"

import { secureGet } from '../utilities/SecureStorage';
import { checkIsLoggedIn } from '../utilities/Account';
import Login from './Login';
import Logout from './Logout';
import AccountPhotos from './AccountPhotos';


export default class Settings extends Component {

    constructor(props) {
      super(props);
      this.state = {
        wantLogIn: false,
        wantLogOut: false,
        isLoggedIn: null,
        accountUsername: null,
      }
    }

    async componentDidMount() {
      let isLoggedIn = await checkIsLoggedIn();
      this.setState(previousState => ({ isLoggedIn: isLoggedIn }));

      let accountUsername = await secureGet('accountUsername');
      console.log(accountUsername);
      if (accountUsername) {
        this.setState(previousState => ({ accountUsername: accountUsername }));
      }
      // // display user's images
      // let sourceData = await getAccountImages();
      // console.log(sourceData);
      // this.setState(previousState => ({ sourceData: sourceData}));
    }

    // FIXME: re-render after exit

    updateLoginState = (wantLogIn, isLoggedIn) => {
      this.setState(previousState => (
        { wantLogIn: wantLogIn, isLoggedIn: isLoggedIn }
      ));
    }

    updateLogoutState = (wantLogOut, isLoggedIn, accountUsername) => {
      this.setState(previousState => (
        { wantLogOut: wantLogOut, isLoggedIn: isLoggedIn, accountUsername: accountUsername }
      ));
    }

    render() {
      if (this.state.isLoggedIn == null) {
        return null;
      } else if (this.state.wantLogIn) {
        return (
          <Login callback={ this.updateLoginState }/>
        );
      } else if (this.state.wantLogOut) {
        return (
          <Logout callback={ this.updateLogoutState }/>
        );
      } else if (this.state.isLoggedIn) {
        if (this.state.accountUsername) {
          return (
            <View>
              <Text style={{margin: 30}}>Current user: {this.state.accountUsername}</Text>
              <Button 
                    title='Log out'
                    onPress={() => this.setState(previousState => ({wantLogOut: true}))}
              />
              <Button
                    title='My images'
                    onPress={() => this.props.navigation.navigate('AccountPhotos')}
              />         
            </View>
          );
        } else {
          return null;
        }
      } else {
        return (
              <SafeAreaView style={{
                  flex: 1,
                  justifyContent: 'center',
                }}>
              <View style={{margin: 30}}>
                <Text style={{margin: 30}}>Welcome, stranger</Text>
                <Button 
                  title='Log in'
                  onPress={() => this.setState(previousState => ({wantLogIn: true}))}
                />
              </View>
            </SafeAreaView>
        );
      }
    }
}
