import React, { Component } from 'react';
import { Text, Image, FlatList, SafeAreaView, StyleSheet, View, ActivityIndicator, Platform } from 'react-native';
import { createBottomTabNavigator } from "react-navigation-tabs";
import { createStackNavigator } from "react-navigation-stack"
import { createAppContainer } from "react-navigation";

import Login from './components/Login';
import { secureGet } from './utilities/SecureStorage';
import { imgur_account_my_images } from './api/Constants';
import RootFeed from "./navigation/RootFeed";
import RootFavorite from "./navigation/RootFavorite";
import RootUpload from "./navigation/RootUpload";
import Settings from './components/Settings';
import Feed from './Feed';
import Favorite from './Favorite'
import AccountPhotos from './components/AccountPhotos';


export class App extends Component {

  constructor(props) {
    super(props);
    this.state = {  checkedLogIn: false, 
                    isLoggedIn: false,
                    accountUsername: null,
                    isLoading: false,
                    isIOS: Platform.OS === "ios" ? true : false,
                  }
  }

  render() {
    console.log("in app component")
    if (this.state.isLoading) {
      return (
        <View>
          <ActivityIndicator style={styles.loading} />
        </View>
      )
    } else {
      return (
        <SafeAreaView style={styles.container}>
          {/* <View > */}
          <View style={styles.navigatorBar}>
            {/* <Text style={{ fontSize: 30 }}>NAVIGATION BAR</Text>
          </View>
          <View style={styles.contentsView}>
            <MainTableView />
          </View>
          <View style={styles.tabBar}>
            <TabBar /> */}
          </View>
          {/* </View> */}
        </SafeAreaView>
      )
    }
  }
}


const TabNavigator = createBottomTabNavigator({
  Feed: {
    screen: createStackNavigator({
      Feed: { screen: Feed },
    }),
  },
  Upload: {
    screen: RootUpload,
    navigationOptions: {
      tabBarOnPress: ({ navigation, defaultHandler }) => {
        console.log("DSFDSFDSFSDFSD")
        navigation.setParams({
          dummy: false
        })
        defaultHandler()
      }
    }
  },
  Favorite: {
    screen: createStackNavigator({
      Favorite: { screen: Favorite },
    }),
  },
});


const AppNavigator = createStackNavigator({
  TabNavigator: {
    screen: TabNavigator,
    headerMode: 'none',
    navigationOptions: {
      headerVisible: false,
      header: null,
  }},
  Settings: Settings,
  AccountPhotos: AccountPhotos,
}, )


export default createAppContainer(AppNavigator);


const styles = StyleSheet.create({
  container: {
    flex: 1
  },
  loading: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center"
  },
  navigatorBar: {
    height: 75,
    alignItems: "stretch",
    backgroundColor: "red"
  },
  tabBar: {
    height: 100,
    alignItems: "stretch",
    backgroundColor: "yellow"
  },
  contentsView: {
    flex: 4
  }
})
