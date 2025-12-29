import React, { Component } from "react";
import { Link } from "react-router-dom";
import "../styles/Navbar.css";  // ⬅️ importe depuis ton répertoire CSS

class Navbar extends Component {
  render() {
    return (
      <nav className="navbar">
        <Link to="/" className="nav-link">Accueil</Link>
        <Link to="/portfolio" className="nav-link">Portfolio</Link>
        <Link to="/contact" className="nav-link">Contact</Link>
      </nav>
    );
  }
}

export default Navbar;