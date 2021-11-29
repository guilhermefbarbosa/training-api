import flask
from model.posts import Post
#import request
app = flask.Flask(__name__)

def __init__(self):
    posts = []
@app.route('/home')
def home():
    post = Post('title1', '01/01/2000', 'Pedro', 'Oi tudo bem bom dia tamo junto')
    post1 = Post('title2', '02/02/2000', 'Marina','Hoje escreveremos sobre coisas muito interessantes')
    post2 = Post('title3', '02/02/2015', 'Caroline', 'Fake news')

    posts = [post, post1, post2]
    return flask.render_template('postlist.html', posts=posts)
@app.route('/new')
def new():
    return flask.render_template('newpost.html')

@app.route('/add', methods=['POST',])
def add():
    app.posts.append(Post(flask.request.form['title'], flask.request.form['created_on'], flask.request.form['author'], flask.request.form['text']))
    return 202


app.run(debug=True)