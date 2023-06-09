from flask import render_template,redirect,request
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def ninjas():
    dojo = Dojo.get_all()
    return render_template('ninjas.html', dojos=dojo)

@app.route('/ninja/create', methods=["POST"])
def ninja_create():
    print(request.form)
    Ninja.save(request.form)
    return redirect('/dojos')
