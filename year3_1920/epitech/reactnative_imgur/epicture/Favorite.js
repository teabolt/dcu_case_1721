import React, { Component } from "react"
import { SafeAreaView, StyleSheet, Text, View } from "react-native"

/*
 * Grid (Collection View)
 * Edit
 */

export default class Favorite extends Component {
  static navigationOptions = {
    title: "Favorite"
  }

  render() {
    return (
      <SafeAreaView style={styles.container}>
        <Text style={{ fontSize: 30 }}>FAVORITE TAB</Text>
      </SafeAreaView>
    )
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#64ebed",
    alignItems: "center",
    justifyContent: "center"
  }
})
