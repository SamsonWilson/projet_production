import React, { Component } from "react";
import Layout from "../components/Layout";
import "../styles/Contact.css";

class Contact extends Component {
  render() {
    return (
      <Layout>
        <section className="contact">
          <h1>Contactez-nous</h1>
          <form>
            <input type="text" placeholder="Nom" />
            <input type="email" placeholder="Email" />
            <textarea placeholder="Votre message"></textarea>
            <button type="submit">Envoyer</button>
          </form>
        </section>
      </Layout>
    );
  }
}

export default Contact;