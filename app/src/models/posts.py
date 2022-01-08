#from .. import db
#from .. import Repo_as_DB
from datetime import datetime


class Posts():

    def __init__(self, title=None, created_on=None, author=None, text=None):
        self.title = title
        self.created_on = created_on
        self.author = author
        self.text = text

    def save(self):
        return True
        #db.session.merge(self)
        #db.session.commit()

    def is_valid(self):
        return self.title is not None and \
               self.author is not None and\
               self.text is not None and \
               self.created_on is not None and\
               self.valid_date()

    def is_equal(self, post):
        return \
            self.title == post.title and\
            self.created_on == post.created_on and\
            self.author == post.author and\
            self.text == post.text

    def valid_date(self):
        try:
            datetime.strptime(self.created_on, "%Y-%m-%d")
            return True
        except:
            return False

    def to_serializable(self):
        return {
                'title': self.title,
                'created_on': self.created_on,
                'author': self.author,
                'text': self.text
                }
