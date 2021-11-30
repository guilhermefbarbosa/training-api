from flask import Blueprint
from flask_restx import Api
from .posts_api import api as api_post

blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(
    blueprint,
    title='training-api',
    version='0.0.1',
    description='Testing exercice for flask apis',
)
api.add_namespace(api_post, path='/posts')
