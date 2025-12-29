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
  <div className="row row-cols-1 row-cols-md-3 g-4">
    <div className="col">
      <div className="card h-100">
        <img src="https://via.placeholder.com/300x200" className="card-img-top" alt="Produit 1" />
        <div className="card-body">
          <h5 className="card-title">Card title</h5>
          <p className="card-text">
            This is a longer card with supporting text below as a natural lead-in to additional content.
            This content is a little bit longer.
          </p>
        </div>
      </div>
    </div>

    <div className="col">
      <div className="card h-100">
        {/* Exemple sans image */}
        <div className="card-body">
          <h5 className="card-title">Card title</h5>
          <p className="card-text">This is a short card.</p>
        </div>
      </div>
    </div>

    <div className="col">
      <div className="card h-100">
        <div className="card-body">
          <h5 className="card-title">Card title</h5>
          <p className="card-text">
            This is a longer card with supporting text below as a natural lead-in to additional content.
          </p>
        </div>
      </div>
    </div>

    <div className="col">
      <div className="card h-100">
        <div className="card-body">
          <h5 className="card-title">Card title</h5>
          <p className="card-text">
            This is a longer card with supporting text below as a natural lead-in to additional content.
            This content is a little bit longer.
          </p>
        </div>
      </div>
    </div>
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