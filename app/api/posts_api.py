import flask
from app.src.repositories.posts import PostsRepository
from app.src import Repo_as_DB
from flask_restx import Namespace, Resource
import json

api = Namespace(
    'posts',
    description='get and crete posts'
)


@api.route('/get')
class Posts(Resource):
    @api.doc(description='Requisição GET para obter todos os Posts em formato LIST (usado para renderizar o html)')
    def get(self):
        items = Repo_as_DB.get_all()
        return flask.make_response(flask.render_template('postlist.html', posts=items), 200, {'Content-Type': 'text/html'})


@api.route('/get_json')
class Posts(Resource):
    @api.doc(description='Requisição GET para obter todos os Posts em formato JSON')
    def get(self):
        items = Repo_as_DB.get_json()
        return flask.make_response(items, 200, {'Content-Type': 'application/json'})
        #return flask.make_response(items, 200, {'Content-Type': 'application/json'})


@api.route('/new')
class Posts(Resource):
    @api.doc(description='Requisição GET para navegar para a tela de inserir novo post')
    def get(self):
        return flask.make_response(flask.render_template('newpost.html'), 200, {'Content-Type': 'text/html'})


@api.route('/add', methods=['POST'])
class Posts(Resource):
    @api.doc(description='Requisição POST para inserir novo post (objeto) no banco de dados')
    def post(self):
        Repo_as_DB.save(title=flask.request.form['title'], created_on=flask.request.form['created_on'], author=flask.request.form['author'], text=flask.request.form['text'])
        print(flask.request.form['created_on'])
        items = Repo_as_DB.get_all()
        return flask.make_response(flask.render_template('postlist.html', posts=items), 200, {'Content-Type': 'text/html'})

