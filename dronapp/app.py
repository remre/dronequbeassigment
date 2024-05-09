from flask import Flask, jsonify
from flask_restful import Api
from flask_cors import CORS
from flask_login import LoginManager
from flask_jwt_extended import JWTManager

from extensions import db
from models.user import User
from resources.dronelist import DroneListResource
from resources.auth import auth_bp
from resources.taskresources import task_bp, TaskResource, TaskExecutionResource, TaskImagesResource,TaskListResource

login_manager = LoginManager()

app = Flask(__name__)
api = Api(app)
CORS(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

# DB configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///uav.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'asdasdasd46465' 

db.init_app(app)
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(task_bp, url_prefix='/api')
jwt = JWTManager(app)

@app.route('/get_user/<username>', methods=['GET'])
def get_user(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({
            'id': user.id,
            'username': user.username,
            'role': user.role
        }), 200
    else:
        return jsonify({'message': 'User not found'}), 404

  
# Register API resources
api.add_resource(DroneListResource, '/api/drones')
api.add_resource(TaskResource, '/api/tasks', '/api/tasks/<int:task_id>')
api.add_resource(TaskExecutionResource, '/api/tasks/<int:task_id>/execute')
api.add_resource(TaskImagesResource, '/api/tasks/<int:task_id>/images')
api.add_resource(TaskListResource, '/tasks')

if __name__ == '__main__':
    app.run(debug=True)
