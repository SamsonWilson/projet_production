import React, { Component } from "react";
import Layout from "../components/Layout";
import { Container, Row, Col, Card, Button } from 'react-bootstrap';
import "../styles/Home.css";

class Home extends Component {
  render() {
    return (
      <Layout>
        {/* ... votre section hero ... */}

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

        {/* ... votre section vidéo ... */}
      </Layout>
    );
  }
}

export default Home;