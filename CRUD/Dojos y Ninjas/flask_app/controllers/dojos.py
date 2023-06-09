from flask import render_template,redirect,request
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def inicio():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template('all_dojos.html', dojos=dojos)

@app.route('/dojos/<int:id>')
def show(id):
    data = {
        "id":id
    }
    dojo = Dojo.get_ninja_from_dojos(data)
    return render_template('one_dojo.html', dojo=dojo)

@app.route('/dojo/create', methods=["POST"])
def dojo_create():
    print(request.form)
    Dojo.save(request.form)
    return redirect('/dojos')
