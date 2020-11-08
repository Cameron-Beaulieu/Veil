import "./App.css";
import React from "react";
import { Component } from "react";
import Webcam from "react-webcam";
import styles from '../src/stylesheet.css'; 

export default class ImageCapture extends Component {
  constructor(props) {
    super(props);
    this.state = { screenshot: null, labels: null, faces: null };
  }

  saveImg(image) {
    // POST request to /saveImg to get the labels from the screenshot
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({"base64str":image}),
    };
    fetch("http://localhost:8000/saveImg", requestOptions)
      .then((response) => response.json())
      .then((json) => {
        this.setState({ labels: json.data });
      });

    setTimeout(() => {

    // GET request to /getImgs to get the faces
    const requestOptions2 = {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    };
    fetch("http://localhost:8000/getImgs", requestOptions2)
      .then((response) => response.json())
      .then((json) => {
        this.setState({ faces: json.data });
      });

    }, 3000);
  }

  screenshot() {
    // access the webcam trough this.refs
    var screenshot = this.refs.webcam.getScreenshot();
    console.log(screenshot);
    this.setState({ screenshot: screenshot });
    this.saveImg(screenshot);
  }

  showFaces() {
    
    console.log(this.state.faces)
    console.log(this.state.labels)

    if(this.state.faces != null && this.state.labels != null)
    {
      let elements = []
    for (var i = 0; i < (this.state.labels).length; i++) {
      
      console.log(i)
      let labelStr = "";

      if (this.state.labels[i].label == "FaceTrainingSet") {
        labelStr = "No mask ";
      } else {
        labelStr = "Mask ";
      }
      elements.push(
        <div className="result">
          <img id="face" src={"data:image/jpg;base64," + this.state.faces[i]} />
          {labelStr}
          {"confidence: " + this.state.labels[i].confidence.substring(0,6)}
        </div>)
      
    }
    return elements
  }
  }

  render() {
    return (
      <div id="container">
        <img id="banner" src="/veil.png" />
        <Webcam id="webcam" screenshotFormat={"image/png"} audio={false} ref="webcam" />
        {this.state.screenshot ? <img id="screenshot" src={this.state.screenshot}/> : null}
        <button id="screenshotBtn" onClick={this.screenshot.bind(this)}>Detect Masks</button>
        {this.state.labels && this.state.faces ? this.showFaces() : null}
        
      </div>
    );
  }
}
