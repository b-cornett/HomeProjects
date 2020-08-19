import React from "react";
import Navbar from "./Navbar";
import { Link } from "react-router-dom";

export default class Header extends React.Component {
  state = {
    isMenuVisible: false,
    menuBarsOpen: true,
  };

  toggleMenu = () => {
    if (this.state.isMenuVisible === false) {
      this.setState({ isMenuVisible: true, menuBarsOpen: false });
    } else {
      this.setState({ isMenuVisible: false, menuBarsOpen: true });
    }
  };

  render() {
    return (
      <>
        <div id="header">
          <div
            className={`menuIcon${this.state.menuBarsOpen ? "" : "Open"}`}
            onClick={this.toggleMenu}
          >
            <div id="bar1" className="menuBar"></div>
            <div id="bar2" className="menuBar"></div>
            <div id="bar3" className="menuBar"></div>
          </div>
          <h1>MONSTER SIM</h1>
          <Link to="Home">
            <img id="logo" src={require("./images/logo192.png")} alt="logo" />
          </Link>
        </div>
        <div id="lineBreak"></div>
        <div className={`menu${this.state.isMenuVisible ? "" : "hidden"}`}>
          <Navbar pages={this.props.pages} />
        </div>
      </>
    );
  }
}
