from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cnpj = db.Column(db.String(14), nullable=True, unique = True)
    email = db.Column(db.String(100), unique=False, nullable=False)
    celular = db.Column(db.String(100), unique=False, nullable = False)
    status = db.Column(db.Boolean, default = False)
