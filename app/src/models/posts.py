from .. import db


class Posts(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        unique=True,
        nullable=False
    )
    title = db.Column(
        db.String,
        primary_key=False,
        unique=False,
        nullable=False
    )
    created_on = db.Column(
        db.String,
        primary_key=False,
        unique=False,
        nullable=False
    )
    author = db.Column(
        db.String,
        primary_key=False,
        unique=False,
        nullable=False
    )
    text = db.Column(
        db.Text,
        primary_key=False,
        unique=False,
        nullable=False
    )

    def __init__(self, title=None, created_on=None, author=None, text=None):
        self.title = title
        self.created_on = created_on
        self.author = author
        self.text = text
