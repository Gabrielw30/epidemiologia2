from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()



class Banco(db.Model):

    __tablename__ = "Banco"
    metodo = db.Column(db.String, nullable=True)
    id = db.Column(db.Integer, primary_key=True)
    beta = db.Column(db.Float, nullable=True)
    img = db.Column(db.String, nullable=True)


