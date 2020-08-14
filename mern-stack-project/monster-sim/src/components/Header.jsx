import React from "react";
import Navbar from "./Navbar";

export default class Header extends React.Component {
  state = {
    isMenuVisible: false,
  };

  toggleMenu = () => {
    if (this.state.isMenuVisible == false) {
      this.setState({ isMenuVisible: true });
    } else {
      this.setState({ isMenuVisible: false });
    }
  };

  render() {
    return (
      <>
        <div id="header">
          <div className="menuIcon" onClick={this.toggleMenu}>
            <div id="bar1" className="menuBar"></div>
            <div id="bar2" className="menuBar"></div>
            <div id="bar3" className="menuBar"></div>
          </div>
          <h1>MONSTER SIM</h1>
          <img id="logo" src={require("./images/logo192.png")} alt="logo" />
        </div>
        <div id="lineBreak"></div>
        <div className={`menu${this.state.isMenuVisible ? "" : "hidden"}`}>
          <Navbar pages={this.props.pages} />
        </div>
      </>
    );
  }
}
