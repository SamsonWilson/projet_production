// src/pages/Home.js
import React, { Component } from "react";
import Layout from "../components/Layout";
import { Container, Row, Col, Card } from 'react-bootstrap';
import "../styles/Home.css";

class Home extends Component {
  render() {
    return (
      <Layout>
  <nav className="navbar navbar-expand-lg navbar-dark sticky-top">
    <div className="container-fluid">
      <a className="navbar-brand" href="#home">STORYTAILORS</a>
      <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-label="Basculer la navigation">
        <span className="navbar-toggler-icon"></span>
      </button>
      <div className="collapse navbar-collapse" id="navbarNav">
        <ul className="navbar-nav ms-auto">
          <li className="nav-item">
            <a className="nav-link active" href="#home">Accueil</a>
          </li>
          <li className="nav-item">
            <a className="nav-link" href="#realisations">Réalisations</a>
          </li>
          <li className="nav-item">
            <a className="nav-link" href="#contact">Contact</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  {/* Section Héro */}
  <section className="hero-section" id="home">
    <video autoPlay muted loop className="background-video">
      <source src="/videos/videos-bg.mp4" type="video/mp4" />
    </video>
    <div className="hero-overlay"></div>
    <div className="hero-content">
      <h1>STORYTAILORS STYLE</h1>
      <p>Production vidéo & storytelling visuel</p>
      <button className="btn-custom-portfolio">Voir le portfolio</button>
    </div>
  </section>

  {/* Section Portfolio */}
  <section className="portfolio-section" id="realisations">
    <div className="container">
      <h2 className="section-title text-center mb-5">Nos Réalisations</h2>

      <div className="portfolio-grid">
        <div className="project-card">
          <div className="card-header">
            <div className="card-icon-wrapper">
              <img src="/icons/film-icon.svg" alt="Film Institutionnel" className="card-icon" />
            </div>
          </div>
          <div className="card-body">
            <h3 className="card-title">Film Institutionnel "Vision"</h3>
            <p className="card-text">Création d'un film corporate percutant pour la présentation des valeurs et de la mission de l'entreprise.</p>
          </div>
        </div>

        {/* Les autres projets suivent le même modèle, avec <img /> auto-fermé */}
      </div>
    </div>
  </section>

  <section className="video-section">
    <div className="container">
      <h2 className="section-title text-center mb-5">🎥 Notre dernière vidéo</h2>
      <div className="video-container">
        <iframe
          src="https://www.youtube.com/embed/dQw4w9WgXcQ"
          title="YouTube video player"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
          allowFullScreen
        ></iframe>
      </div>
    </div>
  </section>
</Layout>

    );
  }
}

export default Home;