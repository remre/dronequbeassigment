from extensions import db


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)
    image_data = db.Column(db.Text, nullable=False)  
