from flask_restful import Resource
from sqlalchemy.orm import joinedload

from extensions import db
from models.drone import Drone


class DroneListResource(Resource):
    def get(self):
            drones = Drone.query.options(joinedload(Drone.tasks)).all()
            return [{'id': drone.id, 'model': drone.model, 'tasks': [task.id for task in drone.tasks]} for drone in drones]
    def post(self):
        args = self.parser.parse_args()
        drone = Drone(model=args['model'])
        db.session.add(drone)
        db.session.commit()
        return {'id': drone.id, 'model': drone.model}, 201
