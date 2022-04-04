from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required",required=True)
video_put_args.add_argument("views", type=int, help="number of views of the video as a int",required=True)
video_put_args.add_argument("likes", type=int, help="number of likes of the video as a int",required=True)

videos = {}

def abort_if_video_id_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404,message="Video could not be found")

def abort_if_video_id_exist(video_id):
    if video_id in videos:
        abort(409,message="Video already exists with given ID")

class Youtube_REST_API(Resource):
    def get(self, video_id: str): #GET = READ data
        abort_if_video_id_doesnt_exist(video_id)
        return videos[video_id] #must be JSON serializable

    def put(self, video_id: str): #PUT = Update data
        abort_if_video_id_exist(video_id)
        args = video_put_args.parse_args()
        videos[video_id]= args
        return videos[video_id], 201
    
    def delete(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        del videos[video_id]
        return '', 204

api.add_resource(Youtube_REST_API,"/video/<int:video_id>")
        
if __name__ == "__main__":
    app.run(debug=True)