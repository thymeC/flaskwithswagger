import os
from datetime import datetime

from flask import Flask, request
from flask_restx import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.dirname(os.path.realpath(__file__))
print(basedir)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'books.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

api = Api(app, doc='/', title='A book API', description='A simple REST API for books')
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(25), nullable=False)
    author = db.Column(db.String(40), nullable=False)
    date_added = db.Column(db.DateTime(), default=datetime.utcnow())

    def __repr__(self):
        return self.title

book_model = api.model(
    'Book',
    {
        'id':fields.Integer(),
        'title':fields.String(),
        'author': fields.String,
        'date_added': fields.String()
    }
)


@api.route('/books')
class Books(Resource):
    @api.marshal_list_with(book_model, code=200, envelope='books')
    def get(self):
        """Get all books"""
        books=Book.query.all()
        # return jsonify({"message": "Hello World"})
        return books

    @api.marshal_with(book_model, code=201, envelope='book')
    def post(self):
        """create new book"""
        data = request.get_json()
        title = data.get('title')
        author = data.get('author')

        new_book = Book(title=title, author=author)
        db.session.add(new_book)
        db.session.commit()

        return new_book



@api.route('/book/<int:id>')
class BookResource(Resource):
    @api.marshal_with(book_model, code=200, envelope='book')
    def get(self, id):
        """Get a book by id"""
        book = Book.query.get_or_404(id)
        return book

    @api.marshal_with(book_model, code=200, envelope='book')
    @api.doc(params={'title': 'A title'})
    def put(self, id):
        """update a book"""
        book_to_update = Book.query.get_or_404(id)
        data = request.get_json()
        book_to_update.title = data.get('title')
        book_to_update.author = data.get('author')
        db.session.commit()

        return book_to_update, 200

    @api.marshal_with(book_model, code=200, envelope='book_deleted')
    def delete(self, id):
        """Delete a book by id"""
        book_to_delete = Book.query.get_or_404(id)
        db.session.delete(book_to_delete)
        db.session.commit()
        return book_to_delete


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'Book': Book
    }


if __name__ == '__main__':
    app.run(debug=True)
