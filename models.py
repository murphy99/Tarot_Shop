from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(600), nullable=True)
    dimensions = db.Column(db.String(14), nullable=True)
    weight = db.Column(db.Float, nullable=False)
    isbn_13 = db.Column(db.String(14), nullable=True)
    isbn_10 = db.Column(db.String(10), nullable=True)
    language = db.Column(db.String(12), nullable=False)
    author = db.Column(db.String(25), nullable=False)
    publisher = db.Column(db.String(50), nullable=False)
    publish_date = db.Column(db.Date, nullable=True)
    publish_edition = db.Column(db.Date, nullable=True)
    image = db.Column(db.String(250), nullable=True)
    qty = db.Column(db.Integer, nullable=False)
