from flask import render_template, flash, redirect, url_for, session, request
from app import app
from app.forms import GameForm, SolveForm
from src.parse import validate_args
from src.puzzle import make_goal_snail, is_solvable
from src.game import Game
from time import perf_counter
from config import COST, RESULT

FIELDS_INT = ["size", "iteration"]
FIELDS_BOOL = ["unsolvable", "uniform", "greedy"]
FIELDS_STR = ["heuristic"]
SESSION_FIELDS = ['size', 'initial_puzzle', 'uniform', 'greedy', 'heuristic', 'time']
MENU = [{"name": "Start", "url": "index"},
        {"name": "Game", "url": "game"}]


def get_input(d):
    args = {}
    for k, v in d.items():
        if k in FIELDS_INT:
            args[k] = int(v)
        elif k in FIELDS_BOOL:
            args[k] = True if v == "y" else False
        elif k in FIELDS_STR:
            args[k] = v
    args['file'] = None
    args['time'] = True
    for field in FIELDS_BOOL:
        if field not in d:
            args[field] = False
    return args


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = GameForm()
    if form.validate_on_submit():
        args = get_input(request.form.to_dict())
        data = validate_args(args)
        if not data:
            flash("Can't parse arguments")
            return render_template('index.html', title='New Game', form=form, menu=MENU)
        if 'size' in session:
            for field, value in zip(SESSION_FIELDS, data):
                session[field] = value
            session.modified = True
        else:
            for field, value in zip(SESSION_FIELDS, data):
                session[field] = value

        return redirect(url_for('game'))
    return render_template('index.html', title='New Game', form=form, menu=MENU)


@app.route('/game', methods=['GET', 'POST'])
def game():
    form = SolveForm()
    if request.method == 'POST':
        goal = tuple(make_goal_snail(session["size"]))
        session["goal"] = goal
        puzzle_solvable = is_solvable(session["size"], session["initial_puzzle"], goal)
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
