from flask import render_template
from flask_login import LoginManager, login_required

from main import app
from models.Usuario import Usuario

# LoginManager é necessário para que a aplicação
# seja capaz de fazer login e logout de usuários
login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('usuarios/login.html')


@app.route('/admin')
@login_required
def admin():
    return render_template('admin.html')


@login_manager.user_loader
def loader_user(iduser):
    return Usuario.query.get(iduser)
