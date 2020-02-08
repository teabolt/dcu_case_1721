import React, { Component } from "react"
import {
  StyleSheet,
  Text,
  View,
  CameraRoll,
  Image,
  SafeAreaView,
  ScrollView,
  TouchableHighlight,
  FlatList,
  Dimensions
} from "react-native"
import PhotoUpload from 'react-native-photo-upload'


const { width } = Dimensions.get("window")

export default class UploadImage extends Component {

  render() {
    return (
      <View style={styles.container}>
        <PhotoUpload
          onPhotoSelect{base64 => {
            if (base64) {
              console.log(base64);
            }
          }}>
          <Image
            style={{
              width: width,
              height: width
            }}
            source={{ uri: this.props.photo.node.image.uri }}
          />
          <Text style={{ fontSize: 30 }}>UPLOAD TAB</Text>
        </PhotoUpload>
      </View>
    )
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1
    // backgroundColor: "#76ed64"
    // backgroundColor: "transparent"
    // alignItems: "center",
    // justifyContent: "center"
  },
  scrollView: {
    flexWrap: "wrap",
    flexDirection: "row"
  }
})
