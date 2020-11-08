import logo from './logo.svg';
import './App.css';
import React from "react";
import { Button } from 'semantic-ui-react'
import { Component } from 'react';
import Webcam from 'react-webcam';

export default class ImageCapture extends Component{

  constructor(props){
      super(props);
      this.state = { screenshot: null }
  }
  
  myApiCall(){
    fetch('https://jsonplaceholder.typicode.com/todos/1')
      .then(response => response.json())
      .then(json => console.log(json))
  }

  screenshot() {
      // access the webcam trough this.refs
      var screenshot = this.refs.webcam.getScreenshot();
      this.setState({screenshot: screenshot});
    }

  render(){

      return (
          <div>   
           <Webcam audio ={false} ref='webcam'/>
           <button onClick={this.screenshot.bind(this)}>Capture Image</button>
           <button onClick={this.myApiCall}>Mask Detection</button>
           { this.state.screenshot ? <img src={this.state.screenshot} /> : null }
          </div>
          )
  }
}
