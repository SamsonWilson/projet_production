import React, { Component } from "react";
import Layout from "../components/Layout";

class Home extends Component {
  render() {
    return (
      <Layout>
        <div style={{ position: "relative", height: "100vh", overflow: "hidden" }}>
          {/* Vidéo de fond */}
          <video
            autoPlay
            muted
            loop
            playsInline
            style={{
              position: "absolute",
              top: 0,
              left: 0,
              width: "100%",
              height: "100%",
              objectFit: "cover",
              zIndex: -1,
            }}
          >
            <source src="/videos/video-bg.mp4" type="video/mp4" />
          </video>

          {/* Texte d'accroche */}
          <div
            style={{
              position: "absolute",
              top: "50%",
              left: "50%",
              transform: "translate(-50%, -50%)",
              color: "white",
              textAlign: "center",
            }}
          >
            <h1 style={{ fontSize: "3rem", fontWeight: "bold", letterSpacing: "2px" }}>
              STORYTAILORS STYLE
            </h1>
            <p style={{ fontSize: "1.2rem" }}>Production vidéo & storytelling visuel</p>
            <button
              style={{
                marginTop: "20px",
                padding: "12px 25px",
                fontSize: "1rem",
                backgroundColor: "#ff5252",
                color: "#fff",
                border: "none",
                borderRadius: "4px",
                cursor: "pointer",
              }}
            >
              Voir le portfolio
            </button>
          </div>
        </div>

        {/* Section suivante */}
        <section style={{ padding: "80px 20px", textAlign: "center" }}>
          <h2>Nos Réalisations</h2>
          <p>Découvrez une sélection de nos clips, court-métrages et publicités.</p>
        </section>
      </Layout>
    );
  }
}

export default Home;