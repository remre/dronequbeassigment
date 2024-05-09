from extensions import db



class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250), nullable=True)
    drone_id = db.Column(db.Integer, db.ForeignKey('drone.id'), nullable=False)
    drone = db.relationship('Drone', backref=db.backref('tasks', lazy=True))
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'drone_id': self.drone_id
    }
