from datetime import datetime

from book_request import db


class Book(db.Document):
    title = db.StringField(max_length=200, required=True, unique=True)


class Request(db.Document):
    book = db.ReferenceField(Book, unique_with='email', required=True)
    email = db.EmailField(required=True)
    timestamp = db.DateTimeField(required=True, default=datetime.utcnow)
