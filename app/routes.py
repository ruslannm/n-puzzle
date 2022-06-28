from flask import render_template, flash, redirect, url_for, session, request
from app import app
from app.forms import GameForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = GameForm()
    if form.validate_on_submit():
        flash("args OK")
        if 'size' in session:
            session['size'] = request.form['generate']
            session.modified = True
        else:
            session['size'] = request.form['generate']
        return redirect(url_for('game'))
    return render_template('index.html', title='New Game', form=form)


@app.route('/game', methods=['GET', 'POST'])
def game():
    return render_template('game.html', title='Home')
