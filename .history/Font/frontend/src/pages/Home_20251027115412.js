import React, { Component } from "react";

class Home extends Component {
  constructor(props) {
    super(props);
    // état initial
    this.state = {
      clicks: 0
    };
  }

  handleClick = () => {
    this.setState({ clicks: this.state.clicks + 1 });
  };

  render() {
    return (
      <div style={{ textAlign: "center", padding: "50px" }}>
        <h1>Bienvenue sur le site du Producteur Vidéo</h1>
        <p>Découvrez nos réalisations et projets audiovisuels.</p>
        <button
          onClick={this.handleClick}
          style={{
            backgroundColor: "#ff5252",
            color: "white",
            border: "none",
            padding: "10px 20px",
            borderRadius: "5px",
            cursor: "pointer",
            marginTop: "20px",
          }}
        >
          Voir le portfolio ({this.state.clicks})
        </button>
      </div>
    );
  }
}

export default Home;