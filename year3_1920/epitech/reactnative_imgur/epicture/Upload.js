import React, { Component } from "react"
import {
  Platform,
  StyleSheet,
  Text,
  View,
  CameraRoll,
  Image,
  ScrollView,
  TouchableHighlight,
  Dimensions,
  Button
} from "react-native"
import * as Permissions from "expo-permissions"
// import PhotoUpload from 'react-native-photo-upload'


/*
 * Modal
 * Album or Camera
 */

const { width } = Dimensions.get("window")

export default class Upload extends Component {
  constructor(props) {
    super(props)
    this.state = {
      photos: [],
      isSelect: false,
      index: null,
      doUpload: false,
    }
  }

  componentDidMount() {
    this.getPhotos()
    console.log(this.state.photos)
  }

  getPhotos = () => {
    // CameraRoll.getPhotos({
    //   first: 300,
    //   assetType: "All",
    //   groupTypes: "All"
    // }).then((r) => this.setState({ photos: r.edges }))
    let promise
    if (Platform.OS === "ios") {
      promise = CameraRoll.getPhotos({
        first: 100,
        assetType: "All",
        groupTypes: "All"
      })
    } else {
      ;(async () => {
        await Permissions.askAsync(Permissions.CAMERA_ROLL)
      })()
      promise = CameraRoll.getPhotos({
        first: 100,
        assetType: "All"
      })
    }
    promise.then((r) => this.setState({ photos: r.edges }))
  }
  //ded0da1b8fcbf36d3c6797bb857a8b046c3a5959
  test() {
    const uri = this.state.photos[this.state.index].node.image.uri
    console.log(uri)
    return uri
  }

  render() {
    if (this.state.isSelect && this.state.doUpload) {
      return null;
    } else if (this.state.isSelect) {
      return (
        <View style={styles.container}>
          {this.state.photos.map((p, i) => {
            if (i == this.state.index) {
              return (
                <Image
                  style={{
                    width: width,
                    height: width
                  }}
                  key={this.state.index}
                  source={{ uri: p.node.image.uri }}
                />
              )
            }
            return null
          })}
          <Text
            style={{
              marginTop: 30,
              fontSize: 40
            }}
          >
            Upload this photo?
          </Text>
          <Button title="Back to Album" onPress={() => this.setState({ isSelect: false })} />
        </View>
        // <View style={styles.container}>
        //   {/* <View> */}
        //   <Image
        //     style={{
        //       width: 500,
        //       height: 500,
        //       alignItems: "center",
        //       justifyContent: "center"
        //     }}
        //     key={this.state.index}
        //     soruce={{ uri: this.test() }}
        //     // soruce={{ uri: this.state.photos[this.state.index].node.image.uri }}
        //   />
        // </View>
      )
    } else {
      return (
        <View style={styles.container}>
          <ScrollView contentContainerStyle={styles.scrollView}>
            {this.state.photos.map((p, i) => {
              return (
                <TouchableHighlight
                  // style={{ opacity: i === this.state.index ? 0.5 : 1 }}
                  key={i}
                  underlayColor="transparent"
                  onPress={() => {
                    this.setState({ index: i, isSelect: true })
                  }}
                >
                  <Image
                    style={{
                      width: width / 3,
                      height: width / 3
                    }}
                    source={{ uri: p.node.image.uri }}
                  />
                </TouchableHighlight>
              )
            })}
          </ScrollView>
        </View>
      )
    }
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center"
  },
  scrollView: {
    flexWrap: "wrap",
    flexDirection: "row"
  }
})
