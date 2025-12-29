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
  <div class="container my-5">
        <h2 class="text-center mb-4">Mon Portfolio</h2>
        <div class="row row-cols-1 row-cols-md-3 g-4">
            <!-- Projet 1 -->
            <div class="col">
                <div class="card h-100">
                    <img src="https://via.placeholder.com/300x200?text=Projet+Web" class="card-img-top" alt="Projet Web">
                    <div class="card-body">
                        <h5 class="card-title">Projet Alpha - Application Web</h5>
                        <p class="card-text">
                            Développement d'une application web dynamique avec des fonctionnalités en temps réel. Technologies : HTML, CSS, JavaScript, Framework X.
                        </p>
                    </div>
                </div>
            </div>

            <!-- Projet 2 (sans image, peut-être une compétence ou un concept) -->
            <div class="col">
                <div class="card h-100">
                    <div class="card-body">
                        <h5 class="card-title">Projet Beta - Design UI/UX</h5>
                        <p class="card-text">
                            Conception d'interfaces utilisateur intuitives et expériences utilisateur fluides pour une application mobile. Outils : Figma, Sketch.
                        </p>
                    </div>
                </div>
            </div>

            <!-- Projet 3 -->
            <div class="col">
                <div class="card h-100">
                    <img src="https://via.placeholder.com/300x200?text=Projet+Mobile" class="card-img-top" alt="Projet Mobile">
                    <div class="card-body">
                        <h5 class="card-title">Projet Gamma - Application Mobile</h5>
                        <p class="card-text">
                            Création d'une application mobile native pour Android et iOS, avec intégration d'API externes.
                        </p>
                    </div>
                </div>
            </div>

            <!-- Projet 4 -->
            <div class="col">
                <div class="card h-100">
                    <img src="https://via.placeholder.com/300x200?text=Analyse+Donnees" class="card-img-top" alt="Analyse de Données">
                    <div class="card-body">
                        <h5 class="card-title">Projet Delta - Analyse de Données</h5>
                        <p class="card-text">
                            Extraction, nettoyage et analyse de grands ensembles de données pour en tirer des insights stratégiques. Outils : Python, Pandas, Tableau.
                        </p>
                    </div>
                </div>
            </div>

            <!-- Projet 5 -->
            <div class="col">
                <div class="card h-100">
                    <img src="https://via.placeholder.com/300x200?text=Developpement+Backend" class="card-img-top" alt="Développement Backend">
                    <div class="card-body">
                        <h5 class="card-title">Projet Epsilon - API Backend</h5>
                        <p class="card-text">
                            Développement d'une API RESTful robuste et scalable pour gérer les données d'une application front-end. Technologies : Node.js, Express, MongoDB.
                        </p>
                    </div>
                </div>
            </div>

            <!-- Projet 6 -->
            <div class="col">
                <div class="card h-100">
                    <img src="https://via.placeholder.com/300x200?text=Marketing+Digital" class="card-img-top" alt="Marketing Digital">
                    <div class="card-body">
                        <h5 class="card-title">Projet Zeta - Stratégie Digitale</h5>
                        <p class="card-text">
                            Élaboration et exécution d'une stratégie de marketing digital complète, incluant SEO, SEM et réseaux sociaux.
                        </p>
                    </div>
                </div>
            </div>

        </div>
    </div>

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