from flask_wtf import FlaskForm
from wtforms import FileField, IntegerField, RadioField, BooleanField, SubmitField
from wtforms.validators import NumberRange
from config import SIZE, ITERATION


class GameForm(FlaskForm):
    size = IntegerField('Generate size', default=3, validators=[NumberRange(min=SIZE, message="")])
    unsolvable = BooleanField("Generate unsolvable size")
    iteration = IntegerField("Number of swapping", default=10, validators=[NumberRange(min=ITERATION, message=f"Acceptable value for generate puzzle: {ITERATION} <= iteration")])
    uniform = BooleanField("Uniform-cost", default=True)
    greedy = BooleanField("Greedy search", default=True)
    heuristic = RadioField("Heuristic function", default="Manhattan_distance", choices=["Manhattan_distance", "Euclidian_distance", "Hamming_distance"])
    submit = SubmitField('Generate puzzle')