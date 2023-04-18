from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from main import app, db
from models import Usuario
from forms import FormularioUsuario
from flask_bcrypt import generate_password_hash
from flask_bcrypt import check_password_hash


@app.route('/user')
def cria_user():
    form = FormularioUsuario(request.form)
    return render_template('projeto/cadastro_usuario.html', form=form)

@app.route('/cadastro_usuario', methods=['POST', 'GET'])
def cadastro_usuario():
    form = FormularioUsuario(request.form)
    usuario = Usuario.query.filter_by(nome=form.nome.data).first()
    if not usuario:
        user = Usuario()
        user.nome=form.nome.data
        user.senha=generate_password_hash(form.senha.data).decode('utf-8')
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    flash('Usuario não logado!')
    return redirect(url_for('login'))


@app.route('/login')
def login():
    form = FormularioUsuario()
    return render_template('projeto/login.html', form=form)


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    form = FormularioUsuario(request.form)
    usuarios = Usuario.query.filter_by(nome=form.nome.data).first()
    senha = check_password_hash(usuarios.senha, form.senha.data)
    if usuarios and senha:
        session['usuario_logado'] = usuarios.nome
        flash(session['usuario_logado'] + 'logado com sucesso!')
        return redirect(url_for('ativos'))
    else:
        session['usuario_logado'] = form.nome.data
        flash(session['usuario_logado'] + ' não logado!')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('login'))