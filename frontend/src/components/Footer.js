import React from "react";

const Footer = ({ author }) => {
  return (
    <footer className="footer text-center">
      <div className="container">
        <div className="row">
          <div className="col-md-4 mb-5 mb-lg-0">
            <h4 className="text-uppercase mb-4">{author}</h4>
            <p className="lead mb-0"></p>
          </div>
          <div className="col-md-4 mb-5 mb-lg-0">
            <h4 className="text-uppercase mb-4">Around the Wizardry World</h4>
            <ul className="list-inline mb-0">
              <li className="list-inline-item">
                <a
                  className="btn btn-outline-light btn-social text-center rounded-circle"
                  href="#"
                >
                  <i className="fab fa-fw fa-facebook-f" />
                </a>
              </li>
              <li className="list-inline-item">
                <a
                  className="btn btn-outline-light btn-social text-center rounded-circle"
                  href="#"
                >
                  <i className="fab fa-fw fa-google-plus-g" />
                </a>
              </li>
              <li className="list-inline-item">
                <a
                  className="btn btn-outline-light btn-social text-center rounded-circle"
                  href="#"
                >
                  <i className="fab fa-fw fa-twitter" />
                </a>
              </li>
              <li className="list-inline-item">
                <a
                  className="btn btn-outline-light btn-social text-center rounded-circle"
                  href="#"
                >
                  <i className="fab fa-fw fa-linkedin-in" />
                </a>
              </li>
              <li className="list-inline-item">
                <a
                  className="btn btn-outline-light btn-social text-center rounded-circle"
                  href="#"
                >
                  <i className="fab fa-fw fa-dribbble" />
                </a>
              </li>
            </ul>
          </div>
          <div className="col-md-4">
            <h4 className="text-uppercase mb-4">About the Books</h4>
            <p className="lead mb-0">
              Fantastic beasts information around the wizardry world and where
              to find them
            </p>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
