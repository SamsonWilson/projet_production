// src/components/Layout.js
import React, { Component } from "react";
import Navbar from "./Navbar";

class Layout extends Component {
  render() {
    return (
      <div>
        {/* Barre de navigation */}
        <Navbar />
        {/* Contenu spécifique à la page */}
        <div style={{ padding: "20px" }}>
          {this.props.children}
        </div>
        {/* Bas de page */}
        <footer
          style={{
            background: "#222",
            color: "#fff",
            textAlign: "center",
            padding: "10px",
            marginTop: "50px"
          }}
        >
          © 2024 Producteur Vidéo — Tous droits réservés
        </footer>
      </div>
    );
  }
}

export default Layout;