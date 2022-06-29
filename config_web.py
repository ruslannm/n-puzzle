import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'n-puzzle-21-school-rgero'
