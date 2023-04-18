# import os
# from primeiro_projeto import main
from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField


class FormularioAtivo(FlaskForm):
    codigo_ativo = StringField('Codigo do ativo', [validators.data_required(), validators.Length(min=1, max=50)])
    quantidade = StringField('Quantidade do ativo', [validators.data_required(), validators.Length(min=1, max=50)])
    preco = StringField('preco do ativo', [validators.data_required(), validators.Length(min=1, max=50)])
    salvar = SubmitField('Salvar')
    
class FormularioUsuario(FlaskForm):
    nome = StringField('username', [validators.data_required(), validators.Length(min=1, max=50)])
    senha = StringField('password', [validators.data_required(), validators.Length(min=1, max=50)])
    salvar = SubmitField('Login')
    cadastro = SubmitField('Cadastrar usuario')