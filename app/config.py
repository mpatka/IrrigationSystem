from flask_sqlalchemy import SQLAlchemy

app_db = SQLAlchemy()


def init_db(app):
    app_db.init_app(app)
    with app.app_context():
        app_db.create_all()
