from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False, unique=True)
    post= db.relationship('Post', backref='Author', lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

class Post(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(200))
    bodyPart= db.Column(db.String(150))
    target = db.Column(db.String())
    equipment = db.Column(db.String())
    gifUrl = db.Column(db.String())
    date_created= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False )

    def __init__(self, name, bodyPart, target, equipment,  gifUrl, user_id):
        self.name = name
        self.bodyPart = bodyPart
        self.target= target
        self.equipment = equipment
        self.gifUrl = gifUrl
        self.user_id = user_id
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def update_db(self):
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    

class Food(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.Integer)
    sugar= db.Column(db.Integer)
    serving_size = db.Column(db.Integer)
    sodium = db.Column(db.Integer)
    potassium_mg= db.Column(db.Integer)
    saturated_fat = db.Column(db.Integer)
    total_fat = db.Column(db.Integer)
    calories = db.Column(db.Integer)
    cholesterol_mg = db.Column(db.Integer)
    protein = db.Column(db.Integer)
    carbs = db.Column(db.Integer)
    date_created= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False )

    def __init__(self, name, sugar, serving_size, sodium, potassium_mg, saturated_fat, total_fat, calories, cholesterol_mg, protein, carbs, user_id):
        self.name = name
        self.sugar = sugar
        self.serving_size= serving_size
        self.sodium = sodium
        self.potassium_mg = potassium_mg
        self.saturated_fat = saturated_fat
        self.total_fat = total_fat
        self.calories = calories
        self.cholesterol_mg = cholesterol_mg
        self.protein = protein
        self.carbs = carbs
        self.user_id = user_id
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def update_db(self):
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    