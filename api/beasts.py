import flask
import connexion
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

# Beasts API
BEASTS = {
    "Niffler": {
        "name": "Niffler",
        "desc": "A Niffler was a creature with a long snout and a coat of black, fluffy fur. They were attracted to shiny things, which made them wonderful for locating treasure, but this also means that they could wreak havoc if kept (or set loose) indoors. Nifflers in general were usually harmless.",
        "image": ""
    },
    "Fairy": {
        "name": "Fairy",
        "desc": "A Fairy is a small human-like creature with large insect-like wings, which are either transparent or multi-coloured. They possess diminutive intelligence, and live mainly in woodlands or glades",
        "image": ""
    },
    "Chimaera": {
        "name": "Chimaera",
        "desc": "The Chimaera is a vicious, bloodthirsty creature with a lion's head, a goat's body and a dragon's tail.",
        "image": ""
    }
}

# Check database connection
def checkdb():
    try:
        results = db.session.query('1').from_statement(text('SELECT 1')).all()
        return jsonify({"Database connection": results})
    except:
        return jsonify({"Database connection": "Failed"})

# Retrieve all beasts
def all():
    return jsonify(BEASTS)

# Create the application instance
app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
app.add_api('beasts.yaml')

# Get the underlying Flask app instance
flask_app = app.app

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username = "forddeza2545",
    password = "!2345678",
    hostname = "forddeza2545.mysql.pythonanywhere-services.com",
    databasename = "forddeza2545$beasts",
)
flask_app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
flask_app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
flask_app.config['SQLALCHEMY_ECHO'] = True

# Create the SQLAlchemy db instance
db = SQLAlchemy(flask_app)

# Main route
@app.route('/')
def home():
    return 'Beasts API'

if __name__ == '__main__':
    app.run()