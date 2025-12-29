import React, { Component } from "react";
import Layout from "../components/Layout";
import "../styles/Portfolio.css";

class Portfolio extends Component {
  render() {
    return (
      <Layout>
        <section className="portfolio">
          <h1>Nos Projets Vidéo</h1>
          <p>Découvrez notre sélection de réalisations.</p>
        </section>
      </Layout>
    );
  }
}

export default Portfolio;