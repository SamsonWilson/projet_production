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
        <section className="intro-section my-5"> {/* Ajout de marge verticale */}
          <Container> {/* Encapsulez le contenu dans un Container pour un meilleur alignement */}
            <h2 className="text-center mb-4">Nos Réalisations</h2> {/* Titre pour la section portfolio */}
            <Row xs={1} md={2} lg={3} className="g-4"> {/* Ajustement des colonnes pour mieux correspondre aux placeholders */}
              {/* Projet 1 */}
              <Col>
                <Card className="h-100">
                  <Card.Img variant="top" src="logo192.png" alt="Film Institutionnel" />
                  <Card.Body>
                    <Card.Title>Film Institutionnel "Vision"</Card.Title>
                    <Card.Text>
                      Création d'un film corporate percutant pour la présentation des valeurs et de la mission de l'entreprise.
                    </Card.Text>
                  </Card.Body>
                </Card>
              </Col>
              {/* Projet 2 (sans image) */}
              <Col>
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
              <Col>
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
              <Col>
                <Card className="h-100">
                  <Card.Img variant="top" src="logo192.png" alt="Clip Musical" />
                  <Card.Body>
                    <Card.Title>Clip Musical "Harmonie"</Card.Title>
                    <Card.Text>
                      Production d'un clip vidéo créatif et esthétique pour un artiste émergent.
                    </Card.Text>
                  </Card.Body>
                </Card>
              </Col>
            </Row>
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