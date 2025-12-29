// src/pages/Home.js
import React, { Component } from "react";
import Layout from "../components/Layout";
import { Container, Row, Col, Card } from 'react-bootstrap';
import "../styles/Home.css";

class Home extends Component {
  render() {
    return (
      <Layout>
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
            {/* Projet 1 */}
            <div className="project-card">
              <div className="card-header">
                <div className="card-icon-wrapper">
                  <img src="/icons/film-icon.svg" alt="Film Institutionnel" className="card-icon" />
                </div>
              </div>
              <div className="card-body">
                <h3 className="card-title">Film Institutionnel "Vision"</h3>
                <p className="card-text">
                  Création d'un film corporate percutant pour la présentation des valeurs et de la mission de l'entreprise.
                </p>
              </div>
            </div>

            {/* Projet 2 */}
            <div className="project-card">
              <div className="card-header">
                <div className="card-icon-wrapper">
                  <img src="/icons/ad-icon.svg" alt="Publicité Digitale" className="card-icon" />
                </div>
              </div>
              <div className="card-body">
                <h3 className="card-title">Publicité Digitale "Éclat"</h3>
                <p className="card-text">
                  Conception et production d'une série de courtes publicités vidéo optimisées pour les réseaux sociaux.
                </p>
              </div>
            </div>

            {/* Projet 3 */}
            <div className="project-card">
              <div className="card-header">
                <div className="card-icon-wrapper">
                  <img src="/icons/tutorial-icon.svg" alt="Tutoriel Animé" className="card-icon" />
                </div>
              </div>
              <div className="card-body">
                <h3 className="card-title">Tutoriel Animé "Guide"</h3>
                <p className="card-text">
                  Réalisation d'un tutoriel vidéo animé expliquant un concept complexe de manière simple et engageante.
                </p>
              </div>
            </div>

            {/* Projet 4 */}
            <div className="project-card">
              <div className="card-header">
                <div className="card-icon-wrapper">
                  <img src="/icons/music-clip-icon.svg" alt="Clip Musical" className="card-icon" />
                </div>
              </div>
              <div className="card-body">
                <h3 className="card-title">Clip Musical "Harmonie"</h3>
                <p className="card-text">
                  Production d'un clip vidéo créatif et esthétique pour un artiste émergent.
                </p>
              </div>
            </div>

            {/* Projet 5 */}
            <div className="project-card">
              <div className="card-header">
                <div className="card-icon-wrapper">
                  <img src="/icons/doc-icon.svg" alt="Documentaire" className="card-icon" />
                </div>
              </div>
              <div className="card-body">
                <h3 className="card-title">Documentaire "Voyage"</h3>
                <p className="card-text">
                  Création d'un documentaire captivant sur des destinations uniques.
                </p>
              </div>
            </div>

            {/* Projet 6 */}
            <div className="project-card">
              <div className="card-header">
                <div className="card-icon-wrapper">
                  <img src="/icons/event-icon.svg" alt="Vidéo Événementielle" className="card-icon" />
                </div>
              </div>
              <div className="card-body">
                <h3 className="card-title">Vidéo Événementielle "Célébration"</h3>
                <p className="card-text">
                  Captation et montage vidéo d'événements spéciaux.
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Section Vidéo YouTube */}
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