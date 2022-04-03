from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class REST_API(Resource):
    def get(self, name: str, age: int):
        return {"name" : f'Hi {name}', "test" : f'you are {age} years old!'} #must be JSON serializable
    
    def post(self):
        return {"data" : "you did a POST request"}


api.add_resource(REST_API,"/api/<string:name>/<int:age>")
        


if __name__ == "__main__":
    app.run(debug=True)