import React from "react";

const BeastsInfo = ({ name, desc, image }) => {
  return (
    <div className="col-md-6 col-lg-4">
      <div className="container text-center">
        <div className="row">
          <div className="col-lg-12 mx-auto">
            <h2 className="text-secondary mb-0">{name}</h2>
            <hr/>
            <img className="img-fluid" src={image} alt="" />
            <p className="mb-5">{desc}</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default BeastsInfo;
