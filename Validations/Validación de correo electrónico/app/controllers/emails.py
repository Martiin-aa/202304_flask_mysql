from flask import flash, render_template, redirect, request
from app import app
from app.models.email import Email


@app.route('/')
def index():
    return render_template("email.html")

@app.route('/process',methods=['POST'])
def process():
    if not Email.is_valid(request.form):
        return redirect('/')
    Email.save(request.form)
    flash("Se ha creado correctamente", "success")
    return redirect('/results')

@app.route('/results')
def results():
    email = Email.get_all()
    return render_template("results.html", emails=email)

@app.route('/destroy/<int:id>')
def destroy_email(id):
    data = {
        "id": id
    }
    Email.destroy(data)
    return redirect('/results')
