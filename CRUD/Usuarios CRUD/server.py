from flask import Flask, render_template, request, redirect
from usuarios import Usuario

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def inicio():
    return redirect('/users')

@app.route('/users')
def usuarios():
    return render_template('usuarios.html', usuarios=Usuario.get_all())

@app.route('/user/new')
def new():
    return render_template('base.html')

@app.route('/user/edit/<int:id>')
def edit(id):
    data = {
        "id":id
    }
    return render_template('editar.html', usuario=Usuario.get_one(data))

@app.route('/user/show/<int:id>')
def show(id):
    data = {
        "id":id
    }
    return render_template('usuario.html', usuario=Usuario.get_one(data))

@app.route('/user/delete/<int:id>')
def delete(id):
    data = {
        "id":id
    }
    Usuario.delete(data)
    return redirect('/users')

@app.route('/user/create', methods=['GET', 'POST'])
def create():
    print(request.form)
    if request.method == 'POST':
        Usuario.save(request.form)
        return redirect('/users')

@app.route('/user/update', methods=['GET', 'POST'])
def update():
    print(request.form)
    if request.method == 'POST':
        Usuario.update(request.form)
        return redirect('/users')
    
if __name__=="__main__":
    app.run(debug=True)
