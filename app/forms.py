from flask_wtf import FlaskForm
from wtforms import FileField, IntegerField, RadioField, BooleanField, SubmitField
from wtforms.validators import NumberRange
from config import SIZE, ITERATION, ERROR_MESSAGE_SIZE, ERROR_MESSAGE_ITERATION, HEURISTIC, HEURISTIC_DEFAULT


class FileForm(FlaskForm):
    file = FileField("Upload file")
    upload = SubmitField('Upload')


class GameForm(FlaskForm):
    generate = BooleanField("Generate puzzle", default=False)
    size = IntegerField('Generate size', default=SIZE, validators=[NumberRange(min=SIZE, message=ERROR_MESSAGE_SIZE)])
    unsolvable = BooleanField("Generate unsolvable size")
    iteration = IntegerField("Number of swapping", default=ITERATION,
                             validators=[NumberRange(min=ITERATION, message=ERROR_MESSAGE_ITERATION)])
    uniform = BooleanField("Uniform-cost", default=True)
    greedy = BooleanField("Greedy search", default=True)
    heuristic = RadioField("Heuristic function", default=HEURISTIC_DEFAULT,
                           choices=HEURISTIC)
    validate = SubmitField('Validate')


class SolveForm(FlaskForm):
    submit = SubmitField('Solve')
