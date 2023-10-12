from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api()


class Main(Resource):
    def get(self):
        return dict(info="Some", num=56)


api.add_resource(Main, "/api")
api.init_app(app)
if __name__ == '__main__':
    app.run(debug=True, port=8888, host='127.0.0.1')
