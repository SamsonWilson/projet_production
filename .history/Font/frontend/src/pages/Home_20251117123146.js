import React, { Component } from "react";
import Layout from "../components/Layout";
import { Container, Row, Col, Card, Button } from 'react-bootstrap'; // Importez les composants nécessaires
import "../styles/Home.css"; // Assurez-vous que ce fichier CSS contient les styles pour le héros, la vidéo, etc.

class Home extends Component {
  render() {
    return (
      <Layout>
        {/* Section Héro avec vidéo en arrière-plan */}
        <div className="hero-section">
          <video autoPlay muted loop playsInline className="background-video">
            <source src="/videos/videos-bg.mp4" type="video/mp4" />
          </video>

          <div className="hero-content">
            <h1>STORYTAILORS STYLE</h1>
            <p>Production vidéo & storytelling visuel</p>
            <Button variant="light">Voir le portfolio</Button> {/* Utilisation du composant Button de React-Bootstrap */}
          </div>
        </div>

        {/* Section Introduction / Portfolio des projets */}
       <section className="intro-section my-5">
          <Container>
            <h2 className="text-center mb-4">Nos Réalisations</h2>

            {/* Wrapper pour le défilement horizontal */}
            <div className="horizontal-scroll-wrapper">
              <Row className="flex-nowrap g-4"> {/* Important: flex-nowrap pour empêcher le retour à la ligne */}
                {/* Projet 1 */}
                <Col xs={12} md={6} lg={4}> {/* Chaque Col doit avoir une largeur définie pour être visible */}
                  <Card className="h-100">
                    <Card.Img variant="top" src="https://via.placeholder.com/300x200?text=Film+Institutionnel" alt="Film Institutionnel" />
                    <Card.Body>
                      <Card.Title>Film Institutionnel "Vision"</Card.Title>
                      <Card.Text>
                        Création d'un film corporate percutant pour la présentation des valeurs et de la mission de l'entreprise.
                      </Card.Text>
                    </Card.Body>
                  </Card>
                </Col>
                {/* Projet 2 (sans image) */}
                <Col xs={12} md={6} lg={4}>
                  <Card className="h-100">
                    <Card.Body>
                      <Card.Title>Publicité Digitale "Éclat"</Card.Title>
                      <Card.Text>
                        Conception et production d'une série de courtes publicités vidéo optimisées pour les réseaux sociaux.
                      </Card.Text>
                    </Card.Body>
                  </Card>
                </Col>
                {/* Projet 3 */}
                <Col xs={12} md={6} lg={4}>
                  <Card className="h-100">
                    <Card.Body>
                      <Card.Title>Tutoriel Animé "Guide"</Card.Title>
                      <Card.Text>
                        Réalisation d'un tutoriel vidéo animé expliquant un concept complexe de manière simple et engageante.
                      </Card.Text>
                    </Card.Body>
                  </Card>
                </Col>
                {/* Projet 4 */}
                <Col xs={12} md={6} lg={4}>
                  <Card className="h-100">
                    <Card.Img variant="top" src="https://via.placeholder.com/300x200?text=Clip+Musical" alt="Clip Musical" />
                    <Card.Body>
                      <Card.Title>Clip Musical "Harmonie"</Card.Title>
                      <Card.Text>
                        Production d'un clip vidéo créatif et esthétique pour un artiste émergent.
                      </Card.Text>
                    </Card.Body>
                  </Card>
                </Col>
                {/* Ajoutez plus de Col ici si vous avez d'autres projets */}
                <Col xs={12} md={6} lg={4}>
                  <Card className="h-100">
                    <Card.Img variant="top" src="https://via.placeholder.com/300x200?text=Documentaire" alt="Documentaire" />
                    <Card.Body>
                      <Card.Title>Documentaire "Nature Urbaine"</Card.Title>
                      <Card.Text>
                        Réalisation d'un court documentaire explorant la biodiversité dans les milieux urbains.
                      </Card.Text>
                    </Card.Body>
                  </Card>
                </Col>
              </Row>
            </div> {/* Fin du wrapper de défilement */}

          </Container>
        </section>


        {/* Section Vidéo YouTube */}
        <section className="video-section my-5"> {/* Ajout de marge verticale */}
          <Container> {/* Encapsulez le contenu dans un Container */}
            <h2 className="text-center mb-4">🎥 Notre dernière vidéo</h2>
            <div className="video-container ratio ratio-16x9"> {/* Utilisation des classes Bootstrap pour le ratio */}
              <iframe
                src="https://www.youtube.com/embed/dQw4w9WgXcQ"
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