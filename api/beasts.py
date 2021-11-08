from flask import jsonify, abort
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
    # Retrieve beast information from database order by Id
    beast = Beast.query \
        .order_by(Beast.id) \
        .all()

    # Serialize the beast object into response
    beast_schema = BeastSchema(many=True)
    data = beast_schema.dump(beast)
    return data

#Update beasts
def update(beast_id, beast):
    # Retrieve beast for updating
    update_beast = Beast.query.filter(Beast.id == beast_id).one_or_none()

    # Check for beast's duplication
    name = beast.get("name")
    existing_beast = (Beast.query.filter(Beast.name == name).one_or_none())

    # Any beast matched?
    if (update_beast is None):
        abort(404, "Beast not found for Id: {beast_id}".format(beast_id=beast_id))

    # Any duplicate beasts?
    elif (existing_beast is not None and existing_beast.id != beast_id):
        abort(409, "Beast {name} already exists".format(name=name))

    # Update beast information
    else:
        # Update Beast in the database
        schema = BeastSchema()
        update = schema.load(beast, session=db.session)
        update.id = update_beast.id
        db.session.merge(update)
        db.session.commit()

        # Return updated beast information
        data = schema.dump(update_beast)
        return data, 200
