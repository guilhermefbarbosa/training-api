import flask
from app.src import db
from app.api import blueprint
import settings
def create_app():

    app = flask.Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://'+\
                                            settings.DB_USER+\
                                            ':'+\
                                            settings.DB_PASSWORD+\
                                            '@'+\
                                            settings.DB_HOST+\
                                            '/'+\
                                            settings.DB_NAME
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    app.register_blueprint(blueprint, url_prefix='/api')
    return app
