import React from "react";
import book from "../images/b.jpg";

const Header = () => {
  return (
    <header className="masthead bg-danger text-white text-center">
      <div className="container">
        <img className="img-fluid mb-5 d-block mx-auto" src={book} alt="b" />
        <h1 className="text-uppercase mb-0">
          Fantastic Beasts &amp; Where to find them
        </h1>
        <hr className="star-info" />
        <h2 className="font-weight-light mb-0">
          Presented by Hogwarts foundation{" "}
        </h2>
      </div>
    </header>
  );
};

export default Header;
