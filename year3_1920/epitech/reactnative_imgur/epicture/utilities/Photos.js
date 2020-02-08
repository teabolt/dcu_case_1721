import React, { Component } from "react"
import {
  Text,
  Image,
  FlatList,
  Dimensions,
  TouchableWithoutFeedback,
  View,
  ImageBackground
} from "react-native"

export default class PhotoList extends Component {
  render() {
    return (
      <FlatList
        numColumns={3}
        data={this.props.dataSource.data}
        renderItem={renderImage}
        ListEmptyComponent={<Text>No images to find here!</Text>}
      />
    )
  }
}
const { width } = Dimensions.get("window")

lastTap = null
function handleDoubleTap(uri) {
  const now = Date.now()
  const DOUBLE_PRESS_DELAY = 300
  if (this.lastTap && now - this.lastTap < DOUBLE_PRESS_DELAY) {
    console.log(uri)
    // this.toggleLike()
  } else {
    this.lastTap = now
  }
}

export function renderImage({ item, index, separators }) {
  if (item) {
    return (
      <TouchableWithoutFeedback
        key={extractUri(item)}
        underlayColor="transparent"
        onPress={() => {
          handleDoubleTap(extractUri(item))
          // console.log(extractUri(item))
        }}
      >
        <View>
          <Image source={{ uri: extractUri(item), width: width, height: width }} />
          {/* <ImageBackground
            source={require("../assets/like.png")}
            // resizeMode="cover"
            style={{ flex: 1 }}
          /> */}
        </View>
      </TouchableWithoutFeedback>
    )
  } else {
    return null
  }
}

function extractUri(item) {
  let uri
  if (item.images) {
    uri = item.images[0].link
  } else {
    uri = item.link
  }
  return uri
}
