from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

user_data = {"Henry" : {"age": 99, "gender": "gay"},
"John": {"age": 70, "gender": "straight"}}

class REST_API(Resource):
    def get(self, name: str):
        return user_data[name] #must be JSON serializable
    
    def post(self):
        return {"data" : "you did a POST request"}

api.add_resource(REST_API,"/api/<string:name>")
        
if __name__ == "__main__":
    app.run(debug=True)