from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, reqparse, Api
import numpy as np
from PIL import Image as PILImage
import os

from extensions import db
from models.task import Task
from models.image import Image



task_bp = Blueprint('task', __name__)
@task_bp.route('/execute_task/<int:task_id>', methods=['POST'])
@jwt_required()
def execute_task(task_id):
    current_user = get_jwt_identity()
  
    return jsonify({'msg': 'Task executed', 'user': current_user})


   
class TaskResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help="Name cannot be blank!")
    parser.add_argument('description', type=str)
    parser.add_argument('drone_id', type=int, required=True, help="Drone ID cannot be blank!")

    def get(self, task_id):
        task = Task.query.get_or_404(task_id)
        return {'id': task.id, 'name': task.name, 'description': task.description, 'drone_id': task.drone_id}

    def post(self):
            args = self.parser.parse_args()
            try:
                task = Task(name=args['name'], description=args['description'], drone_id=args['drone_id'])
                db.session.add(task)
                db.session.commit()
                return {'id': task.id}, 201
            except Exception as e:
                db.session.rollback()
                return {'message': 'Failed to create task', 'error': str(e)}, 400

task_bp = Blueprint('task', __name__)
api = Api(task_bp)

class TaskListResource(Resource):
    def get(self):
        tasks = Task.query.all()
        return jsonify([task.to_dict() for task in tasks])

api.add_resource(TaskListResource, '/tasks')
class TaskExecutionResource(Resource):
    
    def post(self, task_id):
        
        images = self.generate_and_save_images(task_id)
        return {'message': 'Task executed successfully', 'images': [img.image_data for img in images]}

    def generate_and_save_images(self, task_id, num_images=5,):
        images = []
        for _ in range(num_images):
            data = (np.random.rand(1024, 1024, 3) * 255).astype(np.uint8)
            img = PILImage.fromarray(data, 'RGB')
            if not os.path.exists('static/images'):
                os.makedirs('static/images')
            path = f'static/images/task_{task_id}_{np.random.randint(100000)}.png'
            img.save(path)
            
            image_record = Image(task_id=task_id, image_data=path)
            db.session.add(image_record)
            images.append(image_record)
        
        db.session.commit()
        return images

class TaskImagesResource(Resource):
    def get(self, task_id):
        images = Image.query.filter_by(task_id=task_id).all()
        return [{'image_id': img.id, 'image_data': img.image_data} for img in images]

