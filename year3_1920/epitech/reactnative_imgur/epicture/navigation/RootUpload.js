import React, { Component } from "react"
import { Button, Modal, StyleSheet, Text, View } from "react-native"
import Upload from "../Upload"
import SafeAreaView from "react-native-safe-area-view"
import { ActionSheet } from "native-base"

export default class RootUpload extends Component {
  constructor(props) {
    super(props)
    this.state = { isModalVisible: true }
  }

  // componentDidMount() {
  //   console.log("componentDidMount")
  // }
  // componentWillMount() {
  //   console.log("componentWillMount")
  // }
  // componentWillUnmount() {
  //   console.log("componentWillUnmount")
  // }

  modalDismiss() {
    this.setState({ isModalVisible: false })

    // move to Feed tab
    this.props.navigation.navigate("Feed")
  }

  componentWillReceiveProps() {
    console.log("rerender here")
    this.setState({ isModalVisible: true })
  }

  render() {
    console.log("render()")
    return (
      <SafeAreaView>
        <Modal
          animationType="slide"
          transparent={false}
          visible={this.state.isModalVisible}
          onRequestClose={() => {
            this.modalDismiss()
          }}
          onDismiss={console.log("DISMISS 2")}
        >
          <SafeAreaView style={{ flex: 1 }}>
            <View style={styles.button}>
              <Button title="Cancel" onPress={() => this.modalDismiss()} />
              <Button title="Upload" onPress={() => this.null} />
            </View>
            <Upload />
          </SafeAreaView>
        </Modal>
      </SafeAreaView>
    )
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#76ed64",
    alignItems: "center",
    justifyContent: "center"
  },
  button: {
    flexDirection: "row",
    justifyContent: "space-between",
    height: 50
  }
})
