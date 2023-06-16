from flask import render_template, request, redirect, session, flash
from app.models.usuario import Usuario
from app import app
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app) 

@app.route('/')
def index():
    return render_template('/auth/login.html')

@app.route('/register',methods=['POST'])
def register():
    if not Usuario.validate_register(request.form):
        return redirect('/')
    data ={ 
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = Usuario.save(data)
    session['user_id'] = id
    return redirect('/dashboard')

@app.route('/login',methods=['POST'])
def login():
    usuario = Usuario.get_by_email(request.form)

    if not usuario:
        flash("Email invalido","danger")
        return redirect('/')
    if not bcrypt.check_password_hash(usuario.password, request.form['password']):
        flash("Contraseña invalida","danger")
        return redirect('/')
    session['user_id'] = usuario.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': session['user_id']
    }
    return render_template("inicio.html", usuario=Usuario.get_by_id(data))

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
