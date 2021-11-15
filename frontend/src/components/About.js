import React from "react";

const About = ({ title }) => {
  return (
    <section className="bg-danger text-white mb-0" id="about">
      <div className="container">
        <h2 className="text-center text-uppercase text-white">
          Our Foundation
        </h2>
        <hr className="star-light mb-5" />
        <div className="row">
          <div className="col-lg-4 ml-auto">
            <p className="lead">
              Hogwarts foundation is a non-profit organization which receive
              fund from Wizard Government around the world to protect the
              fantastic beasts and all the animals in wizard world
            </p>
          </div>
          <div className="col-lg-4 mr-auto">
            <p className="lead">
              Welcome to Fantastic Beasts and Where to find them social
              information tools to locate any fantastic beasts by category,
              level of the beasts (4 levels) and the location to find them from
              any devices around wizardry world
            </p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default About;
