// src/pages/Home.js

function Home() {
  return (
    <div style={{ textAlign: "center", padding: "50px" }}>
      <h1>Bienvenue sur le site du Producteur Vidéo</h1>
      <p>Découvrez nos réalisations et projets audiovisuels.</p>

      <div style={{ marginTop: "30px" }}>
        <button style={{
          backgroundColor: "#ff5252",
          color: "white",
          border: "none",
          padding: "10px 20px",
          borderRadius: "5px",
          cursor: "pointer"
        }}>
          Voir le portfolio
        </button>
      </div>
    </div>
  );
}

export default Home;