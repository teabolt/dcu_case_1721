// import React, { Component } from "react"
import { createAppContainer } from "react-navigation"
import { createStackNavigator } from "react-navigation-stack"
import Favorite from "../Favorite"

const MainNavigator = createStackNavigator({
  Home: { screen: Favorite }
})

const NavigationFavorite = createAppContainer(MainNavigator)

export default NavigationFavorite
