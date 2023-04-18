from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from main import app, db
from models import Ativos, Usuario


@app.route('/inicio')
def ola():
    return render_template('index.html', titulo='Ativos', ativos=ativos)


@app.route('/ativos')
def ativos():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    ativos = Ativos.query.order_by(Ativos.codigo_ativo)
    return render_template('projeto/ativos.html', ativos=ativos)

@app.route('/atualizar', methods=['POST', ])
def atualizar_ativo():
    ativo = Ativos.query.filter_by(id=request.form['id']).first()
    ativo.codigo_ativo = request.form['codigo']
    ativo.quantidade = request.form['quantidade']
    ativo.preco = request.form['preco']
    
    db.session.add(ativo)
    db.session.commit()
    return redirect(url_for('ativos'))

@app.route('/editar/<int:id>')
def editar_ativo(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar')))
    ativo = Ativos.query.filter_by(id=id).first()
    return render_template('projeto/editar_ativo.html', ativo=ativo)

@app.route('/deletar/<int:id>')
def deletar_ativo(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar')))
    
    Ativos.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Ativo deletado com sucesso')
    return redirect(url_for('ativos'))

@app.route('/cadastrar')
def cadastrar_ativo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    return render_template('projeto/cadastrar.html')

@app.route('/criar_ativo', methods=['POST', ])
def criar_ativo():
    codigo = request.form['codigo']
    quantidade = request.form['quantidade']
    preco = request.form['preco']
    ativo = Ativos()
    ativo.codigo_ativo = codigo
    ativo.preco = preco
    ativo.quantidade = quantidade
    
    db.session.add(ativo)
    db.session.commit()
    
    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    arquivo.save(f'{upload_path}/{ativo.id}_{arquivo.filename}')
    
    return redirect(url_for('ativos'))



@app.route('/user')
def cria_user():
    return render_template('projeto/cadastro_usuario.html')

@app.route('/cadastro_usuario', methods=['POST', 'GET'])
def cadastro_usuario():
    usuario = Usuario.query.filter_by(nome=request.form['username']).first()
    if usuario:
        username = request.form['username']
        password = request.form['password']
        user = Usuario()
        user.nome=username
        user.senha=password
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    flash('Usuario não logado!')
    return redirect(url_for('login'))


@app.route('/login')
def login():
    return render_template('projeto/login.html')


@app.route('/autenticar', methods=['POST', ])
def autenticar():
        
    usuarios = Usuario.query.filter_by(nome=request.form['username']).first()
    if usuarios:
        if request.form['password'] == usuarios.senha:
            session['usuario_logado'] = usuarios.nome
            flash(session['usuario_logado'] + 'logado com sucesso!')
            return redirect(url_for('ativos'))
    else:
        session['usuario_logado'] = request.form['username']
        flash(session['usuario_logado'] + ' não logado!')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('login'))


@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)