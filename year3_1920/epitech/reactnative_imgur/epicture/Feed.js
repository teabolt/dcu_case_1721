import React, { Component } from "react"
import {
  Button,
  SafeAreaView,
  StyleSheet,
  Text,
  View,
  FlatList,
  Platform,
  ActivityIndicator
} from "react-native"
import { withNavigation } from "react-navigation"
import { SearchBar } from "react-native-elements"

import Settings from "./components/Settings"
import { renderImage } from "./utilities/Photos"
import { getFeedImages } from "./api/FeedImages"

/*
 * API connection
 * Search bar hidden
 * Search connection
 * FlatList(TableView)
 */

export default class Feed extends Component {
  static navigationOptions = ({ navigation }) => {
    const { params = {} } = navigation.state
    return {
      title: "Feed",
      // headerTitle:
      // headerStyle: { justifyContent: 'space-between' }
      headerRightContainerStyle: { margin: 5 },
      headerRight: (
        <Button
          onPress={() => params.navigateSettings()}
          title="Settings"
          // color="#fff"
        />
      )
    }
  }

  state = {
    search: "",
    isIos: Platform.OS == "ios" ? true : false,
    dataSource: [],
    navigateSettings: null
  }

  async componentDidMount() {
    // update button
    this.props.navigation.setParams({ navigateSettings: this._navigateSettings.bind(this) })

    // download feed
    console.log("Downloading feed")
    let dataSource = await getFeedImages(this.state.search)
    this.setState((previousState) => ({ dataSource: dataSource }))
  }

  _navigateSettings() {
    this.props.navigation.navigate("Settings")
  }

  updateSearch = (search) => {
    this.setState({ search })
  }

  render() {
    const { search, isIos } = this.state
    return (
      <SafeAreaView style={styles.container}>
        <View>
          <SearchBar
            platform={isIos ? "ios" : "android"}
            placeholder="Search"
            onChangeText={this.updateSearch}
            value={search}
            // on Android the backgroundColor prop makes the app crash
            backgroundColor={isIos ? "transparent" : 0.0}
          />
          {/* <Text style={{ fontSize: 30 }}>FEED TAB</Text> */}
          {/* <Text style={{ fontSize: 20 }}>{search}</Text> */}
          <FlatList
            numColumns={1}
            data={this.state.dataSource.data}
            renderItem={renderImage}
            ListEmptyComponent={
              <View style={{ marginTop: 200, alignItems: "center", justifyContent: "center" }}>
                <ActivityIndicator />
                <Text>No images to find here!</Text>
              </View>
            }
          />
        </View>
      </SafeAreaView>
    )
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1
    // backgroundColor: "pink"
  },
  font: {
    alignItems: "center",
    justifyContent: "center"
  }
})

// export default withNavigation(Feed);
