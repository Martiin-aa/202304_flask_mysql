from flask import flash, render_template, request, redirect
from app.models.survey import Survey
from app import app


@app.route('/')
def get():
    survey = Survey.get_all()
    return render_template('survey.html', surveys=survey)

@app.route('/create/survey', methods=['POST'])
def create_survey():
    if Survey.is_valid(request.form):
        dojo_create = Survey.save(request.form)
        if dojo_create == None:
            flash("Existe un problema.", "danger")
        else:
            flash("Dojo creado Exitosamente", "success")
        return redirect('/results')
    return redirect('/')

@app.route('/results')
def results():
    return render_template('results.html', survey=Survey.get_last_survey())
