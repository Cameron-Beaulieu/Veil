import logo from "./logo.svg";
import "./App.css";
import React from "react";
import { Button } from "semantic-ui-react";
import { Component } from "react";
import Webcam from "react-webcam";

export default class ImageCapture extends Component {
  constructor(props) {
    super(props);
    this.state = { screenshot: null };
  }

  myApiCall() {
    fetch("http://localhost:8000/predict")
      .then((response) => response.json())
      .then((json) => console.log(json));
  }

  saveImg(image) {
    // Simple POST request with a JSON body using fetch
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ base64str: image }),
    };
    console.log(requestOptions);
    fetch("http://localhost:8000/saveImg", requestOptions)
      .then((response) => response.json())
      .then((json) => console.log(json));
  }

  screenshot() {
    // access the webcam trough this.refs
    var screenshot = this.refs.webcam.getScreenshot();
    console.log(screenshot);
    this.setState({ screenshot: screenshot });
    this.saveImg(screenshot);
  }

  showFaces() {
    for (const entry in this.state.labels) {
      let labelStr = "";

      if (entry[1] == "FaceTrainingSet") {
        labelStr = "No mask";
      } else {
        labelStr = "Mask";
      }
      return (
        <div>
          <img src={"/tests/" + entry[0]} />
          {labelStr}
          {"confidence: " + entry[2]}
        </div>
      );
    }
  }

  render() {
    return (
      <div>
        <Webcam screenshotFormat={"image/png"} audio={false} ref="webcam" />
        <button onClick={this.screenshot.bind(this)}>Capture Image</button>
        <button onClick={this.saveImg}>Mask Detection</button>
        {this.state.screenshot ? <img src={this.state.screenshot} /> : null}
        {this.state.labels ? this.showFaces() : null}
      </div>
    );
  }
}
