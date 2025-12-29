import React, { Component } from "react";
import Layout from "../components/Layout";

class Portfolio extends Component {
  render() {
    return (
      <Layout>
        <h1>Nos Projets Vidéo</h1>
        <ul>
          <li>Clip musical A</li>
          <li>Publicité B</li>
          <li>Court métrage C</li>
        </ul>
      </Layout>
    );
  }
}

export default Portfolio;