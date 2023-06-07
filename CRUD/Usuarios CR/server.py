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
def nuevo_usuario():
    return render_template('base.html')

@app.route('/user/create', methods=['GET', 'POST'])
def formulario():
    print(request.form)
    if request.method == 'POST':
        Usuario.save(request.form)
        return redirect('/users')

if __name__=="__main__":
    app.run(debug=True)
