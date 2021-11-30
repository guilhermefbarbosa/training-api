import flask
from app.src import db
from app.api import blueprint

def create_app():

    app = flask.Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:25101991@localhost/training-api-db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    app.register_blueprint(blueprint, url_prefix='/api')
    return app
