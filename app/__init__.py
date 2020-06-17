from flask import Flask


def create_application():
    app = Flask(__name__)
    app.config.from_pyfile('db_config.py')
    return app
