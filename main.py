import flask
from app import create_app,db
from app.src.models.posts import Posts

app = create_app()

@app.route('/home')
def home():
    posts = []#postsRepository.get_all()
    return flask.render_template('postlist.html', posts=posts)

@app.route('/new')
def new():
    return flask.render_template('newpost.html')

@app.route('/add', methods=['POST'])
def add():
    entry = Posts(flask.request.form['title'], flask.request.form['created_on'], flask.request.form['author'], flask.request.form['text'])
    db.session.add(entry)
    db.session.commit()
    return flask.render_template('postlist.html')


app.run(debug=True)
