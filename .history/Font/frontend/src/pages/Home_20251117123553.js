import React, { Component } from "react";
import Layout from "../components/Layout";
import { Container, Row, Col, Card } from 'react-bootstrap'; // Supprimé 'Button' de l'import car nous utiliserons un bouton HTML simple avec CSS
import "../styles/Home.css";

class Home extends Component {
  render() {
    return (
      <Layout>
        {/* Section Héro avec vidéo en arrière-plan */}
        <div className="hero-section">
          <video autoPlay muted loop playsInline className="background-video">
            <source src="/videos/videos-bg.mp4" type="video/mp4" />
          </video>

          {/* Overlay pour assombrir la vidéo et mieux lire le texte */}
          <div className="hero-overlay"></div>

          <div className="hero-content">
            <h1>STORYTAILORS STYLE</h1>
            <p>Production vidéo & storytelling visuel</p>
            {/* Utilisation d'un bouton HTML simple avec une classe CSS personnalisée */}
            <button className="btn-custom-portfolio">Voir le portfolio</button>
          </div>
        </div>

        {/* Section Introduction / Portfolio des projets */}
        <section className="intro-section my-5">
          <Container>
            <h2 className="text-center mb-4 section-title">Nos Réalisations</h2> {/* Ajout d'une classe pour le style du titre */}

            {/* Wrapper pour le défilement horizontal */}
            <div className="horizontal-scroll-wrapper">
              <Row className="flex-nowrap g-4">
                {/* Projet 1 */}
                <Col xs={12} sm={6} md={4} lg={3} className="d-flex"> {/* d-flex pour s'assurer que les cartes ont la même hauteur */}
                  <Card className="h-100 project-card"> {/* Ajout d'une classe pour le style des cartes */}
                    {/* Les images dans l'exemple sont des icônes, donc nous allons remplacer Card.Img par une div avec une icône */}
                    <div className="card-icon-wrapper">
                      <img src="/icons/film-icon.svg" alt="Film Institutionnel" className="card-icon" /> {/* Exemple d'icône */}
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
                {/* Projet 5 (Ajouté pour avoir plus de cartes comme dans l'image) */}
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
                 {/* Projet 6 (Ajouté pour avoir plus de cartes comme dans l'image) */}
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
        <section className="video-section my-5">
          <Container>
            <h2 className="text-center mb-4 section-title">🎥 Notre dernière vidéo</h2> {/* Ajout d'une classe pour le style du titre */}
            <div className="video-container ratio ratio-16x9">
              <iframe
                src="https://www.youtube.com/embed/dQw4w9WgXcQ" // N'oubliez pas de changer cette URL pour votre vraie vidéo !
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