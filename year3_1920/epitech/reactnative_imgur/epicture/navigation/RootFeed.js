// import React, { Component } from "react"
import { createAppContainer } from "react-navigation"
import { createStackNavigator } from "react-navigation-stack"
import Feed from "../Feed"
import Settings from '../components/Settings'
import AccountPhotos from '../components/AccountPhotos';

const MainNavigator = createStackNavigator({
  Feed: { screen: Feed },
})


export default createAppContainer(MainNavigator)
