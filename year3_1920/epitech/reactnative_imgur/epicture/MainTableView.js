import React, { Component } from "react"
import { Platform, StyleSheet, Text, View, ScrollView } from "react-native"
import { SearchBar } from "react-native-elements"

export default class MainTableView extends Component {
  state = {
    search: "",
    platform: Platform.OS,
    currColor: "#FFFF"
  }

  updateSearch = (search) => {
    this.setState({ search })
  }

  render() {
    const { search, platform } = this.state

    //just for testing
    var testBoxes = []
    for (let i = 0; i < 50; i++) {
      testBoxes.push(<View style={styles.testBox} />)
    }

    return (
      <View style={styles.container}>
        <SearchBar
          platform={platform == "ios" ? "ios" : "android"}
          placeholder="Search"
          onChangeText={this.updateSearch}
          value={search}
          containerStyle="tra"
          backgroundColor="transparent"
        />
        <Text style={styles.testFont}> {search} </Text>
        <ScrollView style={styles.scrollView}>
          {/* {testBoxes} */}
          <View style={styles.testBox} />
        </ScrollView>
      </View>
    )
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "transparent"
    // alignItems: "center",
    // justifyContent: "center"
  },
  scrollView: {
    flex: 1
  },
  testBox: {
    flex: 1,
    height: 50,
    width: 400,
    marginBottom: 5,
    backgroundColor: "blue"
  },
  testFont: {
    flex: 0,
    fontSize: 20
  }
})
