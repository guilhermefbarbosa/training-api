import flask
from app.src import Repo_as_DB
from app.api import blueprint
from app.src.repositories.posts import PostsRepository
import settings

def create_app():

    app = flask.Flask(__name__)
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://'+\
    #                                        settings.DB_USER+\
    #                                        ':'+\
    #                                        settings.DB_PASSWORD+\
    #                                        '@'+\
    #                                        settings.DB_HOST+\
    #                                        '/'+\
    #                                        settings.DB_NAME
    #app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    #db.init_app(app)
    app.register_blueprint(blueprint, url_prefix='/api')
    return app
