from flask import render_template, flash, redirect, url_for, session, request
from app import app
from app.forms import GameForm
from src.parse import validate_args

FIELDS_INT = ["size", "iteration"]
FIELDS_BOOL = ["size", "iteration", "unsolvable", "uniform", "greedy", "heuristic"]
FIELDS_STR = ["size", "iteration", "unsolvable", "uniform", "greedy", "heuristic"]

def get_input(d):
    args = {}
    for k, v in request.form.to_dict():
        if k in FIELDS_INT:
            if not v.isdigit():
                flash("Error")

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = GameForm()
    if form.validate_on_submit():
        flash("args OK")
        args = {}
        for k,v in request.form.to_dict():
            if k in FIELDS_INT:


        # size, puzzle, uniform, greedy, heuristic, time = validate_args(
        #     {k: v for k, v in request.form if k in FIELDS}.update({"time": True}))
        print(type(request.form), request.form.to_dict())
        for k, v in request.form.to_dict().items():
            print(k, v)
        # print({k: v for k, v in request.form if k in FIELDS})
        if 'size' in session:
            for field in FIELDS:
                session[field] = request.form[field]
            session.modified = True
        else:
            for field in FIELDS:
                session[field] = request.form[field]
        # size, puzzle, uniform, greedy, heuristic, time = validate_args(
        #     {k: v for k, v in session if k in FIELDS}.update({"time": True}))

        return redirect(url_for('game'))
    return render_template('index.html', title='New Game', form=form)


@app.route('/game', methods=['GET', 'POST'])
def game():
    return render_template('game.html', title='Home')
