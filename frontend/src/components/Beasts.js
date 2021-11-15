import BeastsInfo from "./BeastsInfo";

const Beasts = ({ info }) => {
  return (
    <section className="portfolio" id="portfolio">
      <div className="container">
        <h2 className="text-center text-uppercase text-secondary mb-0"></h2>
        <div className="row">
          {info.status === 200 ? (
            info.data.map((b) => (
              <BeastsInfo 
                name={b.name} 
                image={b.image} 
                desc={b.desc}
              />
            ))
          ):(
            <h3>Loading Beasts Data</h3>
          )}
        </div>
      </div>
    </section>
  );
};

export default Beasts;
