import os
from datetime import datetime

from flask import Flask, jsonify
from flask_restx import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.dirname(os.path.realpath(__file__))
print(basedir)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'books.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

api = Api(app)
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
        books=Book.query.all()
        # return jsonify({"message": "Hello World"})
        return books

    def post(self):
        pass


@api.route('/book<int:id>')
class BookResource(Resource):
    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'Book': Book
    }

if __name__ == '__main__':
    app.run(debug=True)
