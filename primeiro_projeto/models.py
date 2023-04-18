from main import db


class Usuario(db.Model):
    __table_args__ = {'extend_existing': True}
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self) -> str:
        return self.nome

class Ativos(db.Model):
    __table_args__ = {'extend_existing': True}
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    codigo_ativo = db.Column(db.String(50), nullable=False)
    quantidade = db.Column(db.Integer)
    preco = db.Column(db.Float)

    def __repr__(self) -> str:
        return self.codigo_ativo
    
if __name__ == '__main__':
    db.create_all()