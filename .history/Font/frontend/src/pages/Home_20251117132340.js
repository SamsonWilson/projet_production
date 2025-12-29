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
                      <img src="logo192.png" alt="Film Institutionnel" className="card-icon" />
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