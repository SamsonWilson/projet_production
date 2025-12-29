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
   <Container className="my-5">
      <h2 className="text-center mb-4">My Portfolio</h2>
      <Row xs={1} md={3} className="g-4">
        <Col>
          <Card className="h-100">
            <Card.Img variant="top" src="https://via.placeholder.com/300x200?text=Project+1" alt="Project 1" />
            <Card.Body>
              <Card.Title>Project Alpha</Card.Title>
              <Card.Text>
                A dynamic web application built with React and Node.js, focusing on real-time data visualization.
              </Card.Text>
            </Card.Body>
          </Card>
        </Col>
        <Col>
          <Card className="h-100">
            {/* Project without a direct image, could be a logo or icon */}
            <Card.Body>
              <Card.Title>Project Beta</Card.Title>
              <Card.Text>
                An iOS mobile application designed for seamless user experience and offline capabilities.
              </Card.Text>
            </Card.Body>
          </Card>
        </Col>
        <Col>
          <Card className="h-100">
            <Card.Img variant="top" src="https://via.placeholder.com/300x200?text=Project+3" alt="Project 3" />
            <Card.Body>
              <Card.Title>Project Gamma</Card.Title>
              <Card.Text>
                A data analysis project utilizing Python and machine learning to predict market trends.
              </Card.Text>
            </Card.Body>
          </Card>
        </Col>
        <Col>
          <Card className="h-100">
            <Card.Img variant="top" src="https://via.placeholder.com/300x200?text=Project+4" alt="Project 4" />
            <Card.Body>
              <Card.Title>Project Delta</Card.Title>
              <Card.Text>
                A responsive e-commerce website developed with Next.js and integrated with Stripe for payments.
              </Card.Text>
            </Card.Body>
          </Card>
        </Col>
      </Row>
    </Container>
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