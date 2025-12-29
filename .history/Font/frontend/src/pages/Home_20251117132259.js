// src/pages/Home.js
import React, { Component } from "react";
import Layout from "../components/Layout";
import { Container, Row, Col, Card } from 'react-bootstrap'; // Importez uniquement les composants nécessaires de react-bootstrap
import "../styles/Home.css"; // Importez votre fichier CSS personnalisé

class Home extends Component {
  render() {
    return (
      <Layout>
        {/* Section Héro avec vidéo en arrière-plan */}
        <section className="hero-section"> {/* Utilisation de <section> pour la sémantique */}
          <video autoPlay muted loop playsInline className="background-video">
            <source src="/videos/videos-bg.mp4" type="video/mp4" />
          </video>

          {/* Overlay pour assombrir la vidéo et mieux lire le texte */}
          <div className="hero-overlay"></div>

          <div className="hero-content">
            <h1>STORYTAILORS STYLE</h1>
            <p>Production vidéo & storytelling visuel</p>
            <button className="btn-custom-portfolio">Voir le portfolio</button>
          </div>
        </section>

        {/* Section Portfolio des projets (Nos Réalisations) */}
        <section id="realisations" className="portfolio-section py-5"> {/* Ajout d'ID et modification de classe pour plus de clarté */}
          <Container>
            <h2 className="text-center mb-5 section-title">Nos Réalisations</h2> {/* mb-5 pour plus d'espace */}

            {/* Wrapper pour le défilement horizontal */}
            <div className="horizontal-scroll-wrapper">
              <Row className="flex-nowrap g-4 justify-content-center"> {/* justify-content-center pour centrer si peu d'éléments */}
                {/* Projet 1 */}
                <Col xs={12} sm={6} md={4} lg={3} className="d-flex">
                  <Card className="h-100 project-card">
                    <div className="card-icon-wrapper">
                      <img src="/* src/styles/Home.css */

/* --- Variables CSS --- */
:root {
  --primary-color: #f8f9fa; /* Blanc ou gris très clair pour le texte */
  --secondary-color: #ced4da; /* Gris plus clair */
  --dark-bg-color: #212529; /* Couleur de fond sombre pour les sections */
  --card-bg-color: #2c3135; /* Couleur de fond des cartes (légèrement plus claire que le BG) */
  --button-border-color: #f8f9fa; /* Bordure blanche pour le bouton */
  --button-hover-bg-color: #f8f9fa; /* Fond blanc au survol */
  --button-hover-text-color: #212529; /* Texte sombre au survol */
  --section-title-color: #f8f9fa; /* Couleur des titres de section */
  --card-title-color: #f8f9fa; /* Couleur des titres de carte */
  --card-text-color: #ced4da; /* Couleur du texte des cartes */
  --card-icon-circle-bg: #6c757d; /* Fond gris pour le cercle de l'icône */
}

/* --- Styles généraux pour le corps de la page --- */
body {
  background-color: var(--dark-bg-color); /* Fond sombre pour toute la page */
  color: var(--primary-color); /* Couleur de texte par défaut */
  font-family: 'Montserrat', sans-serif; /* Assurez-vous d'importer cette police via Google Fonts dans public/index.html */
  margin: 0;
  padding: 0;
  overflow-x: hidden; /* Empêche le défilement horizontal indésirable de la page */
}

/* Styles pour le Layout (Navbar) - Adaptés à l'image */
.navbar {
    background-color: #2b2b2b !important; /* Couleur de fond de la navbar */
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
}

.navbar-brand, .nav-link {
    color: var(--primary-color) !important;
    font-weight: 600;
}

.nav-link.active {
    color: #007bff !important; /* Exemple de couleur active */
}

/* --- Section Héro --- */
.hero-section {
  position: relative;
  height: 80vh; /* Hauteur de la section héros */
  display: flex;
  justify-content: center;
  align-items: center;
  color: var(--primary-color);
  text-align: center;
  overflow: hidden; /* Assure que la vidéo ne déborde pas */
}

.background-video {
  position: absolute;
  top: 50%;
  left: 50%;
  min-width: 100%;
  min-height: 100%;
  width: auto;
  height: auto;
  object-fit: cover; /* Couvre toute la section */
  transform: translate(-50%, -50%);
  z-index: 1; /* Place la vidéo derrière le contenu */
}

.hero-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* Overlay sombre pour améliorer la lisibilité du texte */
  z-index: 2; /* Place l'overlay entre la vidéo et le contenu */
}

.hero-content {
  position: relative;
  z-index: 3; /* Place le contenu au-dessus de l'overlay */
  padding: 20px;
}

.hero-content h1 {
  font-size: 3.5rem; /* Grande taille de police pour le titre */
  font-weight: 700;
  margin-bottom: 0.5rem;
}

.hero-content p {
  font-size: 1.5rem;
  margin-bottom: 2rem;
  color: var(--secondary-color);
}

.btn-custom-portfolio {
  background-color: transparent; /* Fond transparent */
  color: var(--primary-color); /* Texte blanc */
  border: 2px solid var(--button-border-color); /* Bordure blanche */
  padding: 0.8rem 2rem;
  font-size: 1.1rem;
  text-transform: uppercase;
  letter-spacing: 1px;
  transition: all 0.3s ease;
  border-radius: 5px; /* Coins légèrement arrondis */
  cursor: pointer; /* Indique que c'est cliquable */
}

.btn-custom-portfolio:hover {
  background-color: var(--button-hover-bg-color); /* Fond blanc au survol */
  color: var(--button-hover-text-color); /* Texte sombre au survol */
  text-decoration: none; /* Supprime le soulignement au survol */
}

/* --- Titres de Section (Nos Réalisations, Notre dernière vidéo) --- */
.section-title {
  color: var(--section-title-color);
  font-size: 2.5rem;
  font-weight: 600;
  margin-bottom: 3rem !important; /* Force la marge pour correspondre à l'image */
}

/* --- Section Portfolio (Nos Réalisations) --- */
.portfolio-section {
  background-color: var(--dark-bg-color); /* Fond sombre */
  padding: 4rem 0; /* Padding vertical */
}

.horizontal-scroll-wrapper {
    overflow-x: auto; /* Active le défilement horizontal */
    -webkit-overflow-scrolling: touch; /* Défilement fluide sur iOS */
    padding-bottom: 1rem; /* Espace pour la scrollbar si visible */
}

/* Masquer la scrollbar (cross-browser) */
.horizontal-scroll-wrapper::-webkit-scrollbar {
    display: none; /* Chrome, Safari, Edge */
}
.horizontal-scroll-wrapper {
    -ms-overflow-style: none;  /* IE 10+ */
    scrollbar-width: none;  /* Firefox */
}

.project-card {
  background-color: var(--card-bg-color); /* Fond de carte sombre */
  border: none; /* Pas de bordure par défaut */
  border-radius: 10px; /* Coins arrondis pour les cartes */
  padding: 1.5rem; /* Padding interne */
  color: var(--card-text-color);
  transition: transform 0.2s ease-in-out;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Légère ombre sur les cartes */
}

.project-card:hover {
  transform: translateY(-5px); /* Effet de léger soulèvement au survol */
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3); /* Ombre plus prononcée au survol */
}

.card-icon-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 80px; /* Taille du cercle d'icône */
  height: 80px;
  border-radius: 50%; /* Pour un cercle */
  background-color: var(--card-icon-circle-bg); /* Couleur de fond du cercle */
  margin: 0 auto 1.5rem auto; /* Centrer le cercle et espacement */
  padding: 15px; /* Espace autour de l'icône à l'intérieur du cercle */
}

.card-icon {
  width: 100%; /* L'icône prend 100% de la largeur du wrapper */
  height: 100%;
  object-fit: contain; /* L'icône reste contenue */
  /* Filtre pour rendre l'icône blanche si elle est sombre par défaut */
  filter: invert(100%) sepia(0%) saturate(0%) hue-rotate(0deg) brightness(100%) contrast(100%);
}

.project-card .card-title {
  color: var(--card-title-color);
  font-size: 1.3rem;
  font-weight: 600;
  margin-bottom: 0.75rem;
}

.project-card .card-text {
  font-size: 0.95rem;
  line-height: 1.6;
}

/* --- Section Vidéo YouTube --- */
.video-section {
  background-color: var(--dark-bg-color); /* Fond sombre */
  padding: 4rem 0; /* Padding vertical */
}

.video-container {
  max-width: 900px; /* Limiter la largeur de la vidéo */
  margin: 0 auto; /* Centrer le conteneur vidéo */
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3); /* Ombre pour la vidéo */
  border-radius: 8px; /* Bords légèrement arrondis pour l'iframe */
  overflow: hidden; /* Cache les débordements de l'iframe */
}

/* Règle pour les iframes imbriquées dans .video-container */
.video-container iframe {
    border-radius: 8px; /* Applique les bords arrondis directement à l'iframe */
}

/* --- Responsive Adjustments --- */
@media (max-width: 992px) { /* Pour les écrans de taille moyenne */
    .hero-content h1 {
        font-size: 3rem;
    }
    .hero-content p {
        font-size: 1.3rem;
    }
    .section-title {
        font-size: 2.2rem;
    }
    .project-card .card-title {
        font-size: 1.2rem;
    }
}

@media (max-width: 768px) { /* Pour les tablettes */
  .hero-content h1 {
    font-size: 2.5rem;
  }
  .hero-content p {
    font-size: 1.2rem;
  }
  .btn-custom-portfolio {
    padding: 0.6rem 1.5rem;
    font-size: 1rem;
  }
  .section-title {
    font-size: 2rem;
  }
  .project-card .card-title {
    font-size: 1.1rem;
  }
  .project-card .card-text {
    font-size: 0.85rem;
  }
}

@media (max-width: 576px) { /* Pour les petits mobiles */
    .hero-section {
        height: 60vh; /* Moins haut sur mobile */
    }
    .hero-content h1 {
        font-size: 2rem;
    }
    .hero-content p {
        font-size: 1rem;
    }
    .project-card {
        padding: 1rem;
    }
    .card-icon-wrapper {
        width: 60px;
        height: 60px;
        margin-bottom: 1rem;
    }
    .section-title {
        font-size: 1.8rem;
        margin-bottom: 2rem !important;
    }
}" alt="Film Institutionnel" className="card-icon" />
                    </div>
                    <Card.Body className="text-center">
                      <Card.Title>Film Institutionnel "Vision"</Card.Title>
                      <Card.Text>
                        Création d'un film corporate percutant pour la présentation des valeurs et de la mission de l'entreprise.
                      </Card.Text>
                    </Card.Body>
                  </Card>
                </Col>
                {/* Projet 2 */}
                <Col xs={12} sm={6} md={4} lg={3} className="d-flex">
                  <Card className="h-100 project-card">
                    <div className="card-icon-wrapper">
                      <img src="/icons/ad-icon.svg" alt="Publicité Digitale" className="card-icon" />
                    </div>
                    <Card.Body className="text-center">
                      <Card.Title>Publicité Digitale "Éclat"</Card.Title>
                      <Card.Text>
                        Conception et production d'une série de courtes publicités vidéo optimisées pour les réseaux sociaux.
                      </Card.Text>
                    </Card.Body>
                  </Card>
                </Col>
                {/* Projet 3 */}
                <Col xs={12} sm={6} md={4} lg={3} className="d-flex">
                  <Card className="h-100 project-card">
                    <div className="card-icon-wrapper">
                      <img src="/icons/tutorial-icon.svg" alt="Tutoriel Animé" className="card-icon" />
                    </div>
                    <Card.Body className="text-center">
                      <Card.Title>Tutoriel Animé "Guide"</Card.Title>
                      <Card.Text>
                        Réalisation d'un tutoriel vidéo animé expliquant un concept complexe de manière simple et engageante.
                      </Card.Text>
                    </Card.Body>
                  </Card>
                </Col>
                {/* Projet 4 */}
                <Col xs={12} sm={6} md={4} lg={3} className="d-flex">
                  <Card className="h-100 project-card">
                    <div className="card-icon-wrapper">
                      <img src="/icons/music-clip-icon.svg" alt="Clip Musical" className="card-icon" />
                    </div>
                    <Card.Body className="text-center">
                      <Card.Title>Clip Musical "Harmonie"</Card.Title>
                      <Card.Text>
                        Production d'un clip vidéo créatif et esthétique pour un artiste émergent.
                      </Card.Text>
                    </Card.Body>
                  </Card>
                </Col>
                {/* Projet 5 */}
                <Col xs={12} sm={6} md={4} lg={3} className="d-flex">
                  <Card className="h-100 project-card">
                    <div className="card-icon-wrapper">
                      <img src="/icons/doc-icon.svg" alt="Documentaire" className="card-icon" />
                    </div>
                    <Card.Body className="text-center">
                      <Card.Title>Documentaire "Voyage"</Card.Title>
                      <Card.Text>
                        Création d'un documentaire captivant sur des destinations uniques.
                      </Card.Text>
                    </Card.Body>
                  </Card>
                </Col>
                {/* Projet 6 */}
                <Col xs={12} sm={6} md={4} lg={3} className="d-flex">
                  <Card className="h-100 project-card">
                    <div className="card-icon-wrapper">
                      <img src="/icons/event-icon.svg" alt="Vidéo Événementielle" className="card-icon" />
                    </div>
                    <Card.Body className="text-center">
                      <Card.Title>Vidéo Événementielle "Célébration"</Card.Title>
                      <Card.Text>
                        Captation et montage vidéo d'événements spéciaux.
                      </Card.Text>
                    </Card.Body>
                  </Card>
                </Col>
              </Row>
            </div>
          </Container>
        </section>

        {/* Section Vidéo YouTube */}
        <section className="video-section py-5"> {/* Utilisation de <section> et padding vertical */}
          <Container>
            <h2 className="text-center mb-5 section-title">🎥 Notre dernière vidéo</h2>
            <div className="video-container ratio ratio-16x9">
              <iframe
                src="https://www.youtube.com/embed/dQw4w9WgXcQ" // REMPLACEZ CETTE URL PAR VOTRE VRAIE VIDÉO !
                title="YouTube video player"
                frameBorder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                allowFullScreen
              ></iframe>
            </div>
          </Container>
        </section>
      </Layout>
    );
  }
}

export default Home;