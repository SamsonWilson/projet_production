// src/pages/Home.js
import React, { Component } from "react";
import Layout from "../components/Layout";
import { Container, Row, Col, Card } from 'react-bootstrap';
import "../styles/Home.css";

class Home extends Component {
  render() {
    return (
      <Layout>
          <nav class="navbar navbar-expand-lg navbar-dark sticky-top">
              <div class="container-fluid">
                  <a class="navbar-brand" href="#home">STORYTAILORS</a>
                  <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-label="Basculer la navigation">
                      <span class="navbar-toggler-icon"></span>
                  </button>
                  <div class="collapse navbar-collapse" id="navbarNav">
                      <ul class="navbar-nav ms-auto">
                          <li class="nav-item">
                              <a class="nav-link active" href="#home">Accueil</a>
                          </li>
                          <li class="nav-item">
                              <a class="nav-link" href="#realisations">Réalisations</a>
                          </li>
                          <li class="nav-item">
                              <a class="nav-link" href="#contact">Contact</a>
                          </li>
                      </ul>
                  </div>
              </div>
          </nav>

          <!-- Section Héro -->
          <section class="hero-section" id="home">
              <video autoplay muted loop class="background-video">
                  <source src="/videos/videos-bg.mp4" type="video/mp4">
              </video>
              <div class="hero-overlay"></div>
              <div class="hero-content">
                  <h1>STORYTAILORS STYLE</h1>
                  <p>Production vidéo & storytelling visuel</p>
                  <button class="btn-custom-portfolio">Voir le portfolio</button>
              </div>
          </section>

          <!-- Section Portfolio (Nos Réalisations) -->
          <section class="portfolio-section" id="realisations">
              <div class="container">
                  <h2 class="section-title text-center mb-5">Nos Réalisations</h2>

                  <div class="portfolio-grid">
                      <!-- Projet 1 -->
                      <div class="project-card">
                          <div class="card-header">
                              <div class="card-icon-wrapper">
                                  <img src="/icons/film-icon.svg" alt="Film Institutionnel" class="card-icon">
                              </div>
                          </div>
                          <div class="card-body">
                              <div>
                                  <h3 class="card-title">Film Institutionnel "Vision"</h3>
                                  <p class="card-text">Création d'un film corporate percutant pour la présentation des valeurs et de la mission de l'entreprise.</p>
                              </div>
                          </div>
                      </div>

                      <!-- Projet 2 -->
                      <div class="project-card">
                          <div class="card-header">
                              <div class="card-icon-wrapper">
                                  <img src="/icons/ad-icon.svg" alt="Publicité Digitale" class="card-icon">
                              </div>
                          </div>
                          <div class="card-body">
                              <div>
                                  <h3 class="card-title">Publicité Digitale "Éclat"</h3>
                                  <p class="card-text">Conception et production d'une série de courtes publicités vidéo optimisées pour les réseaux sociaux.</p>
                              </div>
                          </div>
                      </div>

                      <!-- Projet 3 -->
                      <div class="project-card">
                          <div class="card-header">
                              <div class="card-icon-wrapper">
                                  <img src="/icons/tutorial-icon.svg" alt="Tutoriel Animé" class="card-icon">
                              </div>
                          </div>
                          <div class="card-body">
                              <div>
                                  <h3 class="card-title">Tutoriel Animé "Guide"</h3>
                                  <p class="card-text">Réalisation d'un tutoriel vidéo animé expliquant un concept complexe de manière simple et engageante.</p>
                              </div>
                          </div>
                      </div>

                      <!-- Projet 4 -->
                      <div class="project-card">
                          <div class="card-header">
                              <div class="card-icon-wrapper">
                                  <img src="/icons/music-clip-icon.svg" alt="Clip Musical" class="card-icon">
                              </div>
                          </div>
                          <div class="card-body">
                              <div>
                                  <h3 class="card-title">Clip Musical "Harmonie"</h3>
                                  <p class="card-text">Production d'un clip vidéo créatif et esthétique pour un artiste émergent.</p>
                              </div>
                          </div>
                      </div>

                      <!-- Projet 5 -->
                      <div class="project-card">
                          <div class="card-header">
                              <div class="card-icon-wrapper">
                                  <img src="/icons/doc-icon.svg" alt="Documentaire" class="card-icon">
                              </div>
                          </div>
                          <div class="card-body">
                              <div>
                                  <h3 class="card-title">Documentaire "Voyage"</h3>
                                  <p class="card-text">Création d'un documentaire captivant sur des destinations uniques.</p>
                              </div>
                          </div>
                      </div>

                    
                      <div class="project-card">
                          <div class="card-header">
                              <div class="card-icon-wrapper">
                                  <img src="/icons/event-icon.svg" alt="Vidéo Événementielle" class="card-icon">
                              </div>
                          </div>
                          <div class="card-body">
                              <div>
                                  <h3 class="card-title">Vidéo Événementielle "Célébration"</h3>
                                  <p class="card-text">Captation et montage vidéo d'événements spéciaux.</p>
                              </div>
                          </div>
                      </div>
                  </div>
              </div>
          </section>

          <section class="video-section">
              <div class="container">
                  <h2 class="section-title text-center mb-5">🎥 Notre dernière vidéo</h2>
                  <div class="video-container">
                      <iframe
                          src="https://www.youtube.com/embed/dQw4w9WgXcQ"
                          title="YouTube video player"
                          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                          allowfullscreen>
                      </iframe>
                  </div>
              </div>
          </section>

          <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
      </Layout>
    );
  }
}

export default Home;