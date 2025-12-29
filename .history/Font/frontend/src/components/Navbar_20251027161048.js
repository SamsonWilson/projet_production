import React, { Component } from "react";
import { Link } from "react-router-dom";

class Navbar extends Component {
  render() {
    return (
      <nav
        style={{
          background: "#B81515FF;",
          padding: "15px",
          display: "flex",
          justifyContent: "center",
          gap: "20px"
        }}
      >
        <Link to="/" style={{ color: "white", textDecoration: "none" }}>
          Accueil
        </Link>
        <Link to="/portfolio" style={{ color: "white", textDecoration: "none" }}>
          Portfolio
        </Link>
        <Link to="/contact" style={{ color: "white", textDecoration: "none" }}>
          Contact
        </Link>
      </nav>
    );
  }
}

export default Navbar;