import React, { Component } from "react";
import { Link } from "react-router-dom";
import "../styles/Navbar.css";

class Navbar extends Component {
  render() {
    return (
      <nav className="navbar">
        <div className="nav-container">
          <Link to="/" className="nav-logo">
            Producteur Vidéo
          </Link>
          <div className="nav-links">
            <Link to="/" className="nav-link">Accueil</Link>
            <Link to="/portfolio" className="nav-link">Portfolio</Link>
            
            <Link to="/contact" className="nav-link">Contact</Link>
          </div>
        </div>
      </nav>
    );
  }
}

export default Navbar;