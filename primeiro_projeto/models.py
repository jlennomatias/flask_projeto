from datetime import datetime
from main import db



class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(50), nullable=False)

    def __repr__(self) -> str:
        return self.nome

class Ativos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    codigo_ativo = db.Column(db.String(50), nullable=False)
    quantidade = db.Column(db.Integer)
    preco = db.Column(db.Float)

    def __repr__(self) -> str:
        return self.codigo_ativo
    