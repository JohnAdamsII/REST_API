from email import message
from attr import fields
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer,nullable=False)
    likes = db.Column(db.Integer,nullable=False)

    def __repr__(self) -> str:
        return f'{name=} {response.url=} {views=} {likes=}'

# db.create_all() #only needs to happen once or will be deleted

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required",required=True)
video_put_args.add_argument("views", type=int, help="number of views of the video as a int",required=True)
video_put_args.add_argument("likes", type=int, help="number of likes of the video as a int",required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of the video")
video_update_args.add_argument("views", type=int, help="number of views of the video as a int")
video_update_args.add_argument("likes", type=int, help="number of likes of the video as a int")

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer  
}

class VideoREST_API(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id: str): #GET = READ data
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404,message='Could not find video with that id')
        return result

    @marshal_with(resource_fields)
    def put(self, video_id: str): #PUT = Update data
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409,message='Video id taken')
        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201

    @marshal_with(resource_fields)
    def patch(self, video_id): #UPDATE something by Video ID
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(409,message='video doesnt exist, cannot update')
        if args['name']:
            result.name = args['name']
        if args['views']:
            result.views = args['views']
        if args['likes']:
            result.likes = args['likes']
        
        db.session.commit()

        return result

    def delete(self, video_id): #TO DO: https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/
        return '', 204

api.add_resource(VideoREST_API,"/video/<int:video_id>")
        
if __name__ == "__main__":
    app.run(debug=True)