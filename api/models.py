from datetime import datetime
from config import db, ma

class Beast(db.Model):
    __tablename__ = 'beast'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True)
    desc = db.Column(db.String(300))
    image = db.Column(db.String(200))
    create_timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class BeastSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Beast
        load_instance = True