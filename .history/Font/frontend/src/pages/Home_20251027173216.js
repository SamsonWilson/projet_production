import React, { Component } from "react";
import Layout from "../components/Layout";
import "../styles/Home.css";

class Home extends Component {
  render() {
    return (
      <Layout>
        <div className="hero-section">
          <video autoPlay muted loop playsInline className="background-video">
            <source src="/videos/videos-bg.mp4" type="video/mp4" />
          </video>

          <div className="hero-content">
            <h1>STORYTAILORS STYLE</h1>
            <p>Production vidéo & storytelling visuel</p>
            <button>Voir le portfolio</button>
          </div>
        </div>

        <section className="intro-section">
            <h2>Nos Réalisations</h2>
            <div className="portfolio-grid">
                {portfolioItems.map((item, index) => (
                <div className="card" key={index}>
                    <img src={item.image} alt={item.title} className="card-img" />
                    <div className="card-body">
                    <h5 className="card-title">{item.title}</h5>
                    <p className="card-text">{item.description}</p>
                    </div>
                </div>
                ))}
            </div>
</section>


<section className="video-section">
  <h2>🎥 Ma vidéo YouTube</h2>
  <div className="video-container">
    <iframe
      width="560"
      height="315"
      src="https://www.youtube.com/embed/dQw4w9WgXcQ"
      title="YouTube video player"
      frameBorder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
      allowFullScreen
    ></iframe>
  </div>
</section>

      </Layout>
    );
  }
}

export default Home;