from flask import Flask, request
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app)


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

if __name__ == '__main__':
    # if debug=True, update of code will reflect on web
    app.run(debug=True)