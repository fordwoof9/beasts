import React, { useEffect, useState } from "react";
import Nav from "./components/Nav";
import Header from "./components/Header";
import Beasts from "./components/Beasts";
import About from "./components/About";
import Footer from "./components/Footer";
import Copyright from "./components/Copyright";
import axios from "axios";

function App() {
  const [getMessage, setGetMessage] = useState({});
  useEffect(() => {
    axios
      .get("https://forddeza2545.pythonanywhere.com/v1/beast")
      .then((response) => {
        console.log("Beasts infor retrieval successful", response);
        setGetMessage(response);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  return (
    <div className="App">
      <Nav title="Fantastic Beasts" />
      <Header />
      <Beasts info={getMessage} />
      <Footer author={"Newt Scamander and Someone"} />
      <Copyright />
    </div>
  );
}

export default App;
