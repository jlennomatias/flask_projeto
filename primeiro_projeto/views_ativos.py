from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from main import app, db
from models import Ativos
from forms import FormularioAtivo

@app.route('/')
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
    form = FormularioAtivo(request.form)
    
    if form.validate_on_submit():
        ativo = Ativos.query.filter_by(id=request.form['id']).first()
        
        ativo.codigo_ativo = form.codigo_ativo.data
        ativo.quantidade = form.quantidade.data
        ativo.preco = form.preco.data
        
        db.session.add(ativo)
        db.session.commit()
        
    return redirect(url_for('ativos'))

@app.route('/editar/<int:id>')
def editar_ativo(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar')))
    ativo = Ativos.query.filter_by(id=id).first()
    
    form = FormularioAtivo()
    form.codigo_ativo.data = ativo.codigo_ativo
    form.quantidade.data = ativo.quantidade
    form.preco.data = ativo.preco
    
    return render_template('projeto/editar_ativo.html', id=id, form=form)

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
    form = FormularioAtivo()
    return render_template('projeto/cadastrar.html', form=form)

@app.route('/criar_ativo', methods=['POST', ])
def criar_ativo():
    form = FormularioAtivo(request.form)
    
    if form.validate_on_submit():
        return redirect(url_for("ativos"))
    
    codigo = form.codigo_ativo.data
    quantidade = form.quantidade.data
    preco = form.preco.data
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


@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)