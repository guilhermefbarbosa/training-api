import flask
from app.src.repositories.posts import PostsRepository
from flask_restx import Namespace, Resource
import json

api = Namespace(
    'posts',
    description='get and crete posts'
)


@api.route('/get')
class Posts(Resource):
    @api.doc()
    def get(self):
        items = PostsRepository.get_all()
        return flask.make_response(flask.render_template('postlist.html', posts=items), 200, {'Content-Type': 'text/html'})


@api.route('/get_json')
class Posts(Resource):
    @api.doc()
    def get(self):
        items = json.dumps(PostsRepository.get_json())
        return flask.make_response(items, 200, {'Content-Type': 'application/json'})


@api.route('/new')
class Posts(Resource):
    @api.doc()
    def get(self):
        return flask.make_response(flask.render_template('newpost.html'), 200, {'Content-Type': 'text/html'})


@api.route('/add', methods=['POST'])
class Posts(Resource):
    @api.doc()
    def post(self):
        PostsRepository.save(flask.request.form['title'], flask.request.form['created_on'], flask.request.form['author'], flask.request.form['text'])
        items = PostsRepository.get_all()
        return flask.make_response(flask.render_template('postlist.html',posts=items), 200, {'Content-Type': 'text/html'})

