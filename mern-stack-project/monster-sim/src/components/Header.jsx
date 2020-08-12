import React from "react";
import Navbar from "./Navbar";

export default class Header extends React.Component {
  render() {
    return (
      <>
        <div id="header">
          <Navbar pages={this.props.pages} />
          <div className="menuIcon">
            <div id="bar1" className="menuBar"></div>
            <div id="bar2" className="menuBar"></div>
            <div id="bar3" className="menuBar"></div>
          </div>
          <h1>MONSTER SIM</h1>
          <img id="logo" src={require("./images/logo192.png")} alt="logo" />
        </div>
        <div id="lineBreak"></div>
      </>
    );
  }
}
