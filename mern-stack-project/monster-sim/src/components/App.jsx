import React from "react";
import Header from "./Header";
import Footer from "./Footer";
import Home from "./Home";
import About from "./About";
import Simulation from "./Simulation";
import { Route, Switch } from "react-router";
import { BrowserRouter } from "react-router-dom";

const pages = [
  { name: "home", label: "Home" },
  { name: "about", label: "About" },
  { name: "simulation", label: "Simulation" },
];

export default class App extends React.Component {
  render() {
    return (
      <>
        <BrowserRouter>
          <Header pages={pages} />
          <Switch>
            <Route exact path="/simulation" component={Simulation} />
            <Route exact path="/about" component={About} />
            <Route exact path="" component={Home} />
          </Switch>
        </BrowserRouter>
        <Footer />
      </>
    );
  }
}
