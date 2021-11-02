from flask import jsonify
from config import db
from models import Beast, BeastSchema
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