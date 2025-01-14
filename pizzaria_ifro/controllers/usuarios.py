from flask import render_template, request, redirect, flash, Blueprint, url_for
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from utils import db

from models.Usuario import Usuario

bp_usuarios = Blueprint('usuarios', __name__, template_folder='templates')


@bp_usuarios.route('/recovery')
def recovery():
    usuarios = Usuario.query.all()
    return render_template('usuarios/usuarios_recovery.html', usuarios=usuarios)


@bp_usuarios.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == "GET":
        return render_template('usuarios/usuarios_create.html')
    if request.method == "POST":
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        csenha = request.form.get('csenha')
        if senha == csenha:
            usuario = Usuario(nome, email,generate_password_hash(senha))
            db.session.add(usuario)
            db.session.commit()
            return redirect(url_for('.recovery'))
            #return redirect('/usuarios/recovery')
        else:
            flash('As senhas não são iguais', 'red-500')
            return redirect(url_for('.create'))


@bp_usuarios.route('/autenticar', methods=['GET', 'POST'])
def autenticar():
    if request.method == "POST":
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        user = Usuario.query.filter_by(username=usuario).first()
        if check_password_hash(user.senha, senha):
            login_user(user)
            return redirect(url_for('index'))
        else:
            return redirect('/login')

    return render_template('usuarios/login.html')


@bp_usuarios.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))