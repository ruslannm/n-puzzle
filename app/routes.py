from flask import render_template, flash, redirect, url_for, session, request
from app import app
from app.forms import GameForm, SolveForm, FileForm
from src.parse import validate_args
from src.puzzle import make_goal_snail, is_solvable
from src.game import Game
from time import perf_counter
from config import COST, RESULT
import os
from werkzeug.utils import secure_filename

FIELDS_INT = ["size", "iteration"]
FIELDS_BOOL = ["unsolvable", "uniform", "greedy", "attempt"]
FIELDS_STR = ["heuristic"]
SESSION_FIELDS = ['size', 'initial_puzzle', 'uniform', 'greedy', 'heuristic', 'time', "unsolvable", 'iteration',
                  'attempt', 'file']
MENU = [{"name": "Start", "url": "index"},
        {"name": "Game", "url": "game"}]


def get_input(d):
    args = {k: int(v) for k, v in d.items() if k in FIELDS_INT}
    for k in FIELDS_BOOL:
        args[k] = True if d.get(k, None) == "y" else False
    args['heuristic'] = d["heuristic"]
    args['time'] = True
    if d.get("generate", None) == "y":
        args["file"] = None
        session["file"] = None
        session["filename"] = None
    else:
        args["file"] = session["file"]
    return args


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    file_form = FileForm()
    if file_form.validate_on_submit() and file_form.upload.data:
        f = file_form.file.data
        filename = secure_filename(f.filename)
        file = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config["UPLOAD_FOLDER"], filename)
        f.save(file)
        session["file"] = file
        session["filename"] = filename
        flash(f"{filename} uploaded", category='success')
        return redirect(url_for('index'))
    form = GameForm()
    if form.validate_on_submit() and form.validate.data:
        args = get_input(request.form.to_dict())
        data = validate_args(args)
        if not data:
            if session["filename"]:
                flash(f"Can't parse file {session['filename']}", category='error')
            else:
                flash("Can't parse arguments", category='error')
            return render_template('index.html', title='New Game', file_form=file_form, form=form, menu=MENU)
        if 'size' in session:
            for field, value in zip(SESSION_FIELDS, data):
                session[field] = value
            session.modified = True
        else:
            for field, value in zip(SESSION_FIELDS, data):
                session[field] = value

        return redirect(url_for('game'))
    session["upload"] = False
    return render_template('index.html', title='New Game', file_form=file_form, form=form, menu=MENU)


@app.route('/game', methods=['GET', 'POST'])
def game():
    form = SolveForm()
    if request.method == 'POST':
        goal = tuple(make_goal_snail(session["size"]))
        session["goal"] = goal
        puzzle_solvable = is_solvable(session["size"], session["initial_puzzle"], goal)
        if not puzzle_solvable and not session["attempt"]:
            solution = ((RESULT["puzzle_solvable"], puzzle_solvable), [])
        else:
            game = Game(session["size"], session["initial_puzzle"], session["goal"], COST, session["heuristic"],
                        session["uniform"], session["greedy"])
            t_start = perf_counter()
            success, total_number_opened, max_number_opened, path_to_goal = game.solve_a_star()
            t_work = perf_counter() - t_start
            solution = ((RESULT['success'], success), (RESULT["total_number_opened"], total_number_opened),
                        (RESULT["max_number_opened"], max_number_opened),
                        (RESULT["len(path_to_goal)"], len(path_to_goal) - 1),
                        (RESULT["t_work"], t_work),
                        (RESULT["puzzle_solvable"], puzzle_solvable), (RESULT["path_to_goal"], path_to_goal))
        return render_template('game.html', title='Game', menu=MENU, form=form, solution=solution)
    return render_template('game.html', title='Game', menu=MENU, form=form, solution=None)
