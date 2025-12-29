import React, { Component } from "react";
import Navbar from "./Navbar";
import "../styles/Layout.css";

class Layout extends Component {
  render() {
    return (
      <div className="layout">
        <Navbar />
        <div className="content">{this.props.children}</div>
        <footer className="footer">
          © 2024 Producteur Vidéo — Tous droits réservés
        </footer>
      </div>
    );
  }
}

export default Layout;