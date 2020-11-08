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

  writeImg() {
    // Example POST method implementation:
    async function postData(url = "", data = {}) {
      // Default options are marked with *
      const response = await fetch(url, {
        method: "POST", // *GET, POST, PUT, DELETE, etc.
        mode: "cors", // no-cors, *cors, same-origin
        cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
        credentials: "same-origin", // include, *same-origin, omit
        headers: {
          "Content-Type": "application/json",
          // 'Content-Type': 'application/x-www-form-urlencoded',
        },
        redirect: "follow", // manual, *follow, error
        referrerPolicy: "no-referrer", // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
        body: JSON.stringify(data), // body data type must match "Content-Type" header
      });
      return response.json(); // parses JSON response into native JavaScript objects
    }

    postData("https://example.com/answer", { answer: 42 }).then((data) => {
      console.log(data); // JSON data parsed by `data.json()` call
    });
  }

  screenshot() {
    // access the webcam trough this.refs
    var screenshot = this.refs.webcam.getScreenshot();
    console.log(screenshot)
    this.setState({ screenshot: screenshot });
  }

  render() {
    return (
      <div>
        <Webcam audio={false} ref="webcam" />
        <button onClick={this.screenshot.bind(this)}>Capture Image</button>
        <button onClick={this.myApiCall}>Mask Detection</button>
        {this.state.screenshot ? <img src={this.state.screenshot} /> : null}
      </div>
    );
  }
}
