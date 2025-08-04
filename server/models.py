from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String,nullable = False)
    image = db.Column(db.String,nullable = False, default='default_plant_image.jpg')
    price =db.Column(db.Float, default=0.0)

    def __init__(self, name,image=None, price=None):
        self.name = name
        self.image = image
        self.price = price
 

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "image": self.image,
            "price": self.price
        }