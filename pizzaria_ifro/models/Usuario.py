from flask_login import UserMixin
from utils import db


class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)

    def __init__(self, username, email, senha):
        self.username = username
        self.email = email
        self.senha = senha

    def __repr__(self):
        return self.nome
