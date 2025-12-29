import React, { Component } from "react";
import Layout from "../components/Layout";
import "../styles/Home.css";

class Home extends Component {
  render() {
    return (
      <Layout>
        <div className="hero-section">
          <video autoPlay muted loop playsInline className="background-video">
            <source src="../assets/videos/video-bg.mp4" type="video/mp4" />
          </video>

          <div className="hero-content">
            <h1>STORYTAILORS STYLE</h1>
            <p>Production vidéo & storytelling visuel</p>
            <button>Voir le portfolio</button>
          </div>
        </div>

        <section className="intro-section">
          <h2>Nos Réalisations</h2>
          <p>Découvrez une sélection de nos clips, publicités et courts métrages.</p>
        </section>
      </Layout>
    );
  }
}

export default Home;