from flask_wtf import FlaskForm
from wtforms import FileField, IntegerField, RadioField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class GameForm(FlaskForm):
    generate = IntegerField('Generate size')
    unsolvable = BooleanField("Generate unsolvable size")
    iteration = IntegerField("Number of swapping")
    method = RadioField("Method", default="A*", choices=["uniform-cost", "greedy search", "A*"])
    heuristic = RadioField("Heuristic function", default="Manhattan_distance", choices=["Manhattan_distance", "Euclidian_distance", "Hamming_distance"])
    submit = SubmitField('Generate puzzle')