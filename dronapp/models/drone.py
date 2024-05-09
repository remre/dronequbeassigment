from extensions import db


class Drone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50), nullable=False)
