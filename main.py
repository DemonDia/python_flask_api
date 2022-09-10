from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
# configuring marshmellow
ma = Marshmallow(app)

# wrap app in the API
# =================configuring SQLAlchemy=================
# the destination of the data source
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

# the Video model
class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    likes = db.Column(db.Integer, nullable=False)
    views = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video[id={self.id}, name={self.name}, likes={self.likes}, views={self.views}]"
db.create_all()

# the Video schema (for JSON formatting)
class VideoSchema(ma.Schema):
    class Meta:
        fields = ("id","name","likes","views")
# Creating instance of schemas
# when theres a single instance to be returned
video_schema = VideoSchema(many = False)
# when there are multiple instances to be returned
videos_schema = VideoSchema(many = True)


# =================app routes=================

# to get ALL the videos in the db
@app.route("/video", methods=["GET"])
def getAll():
    result = Video.query.all()
    return_results = videos_schema.dump(result)
    # results = [i.tojson() for i in result]
    return jsonify(
        {
            "success": True,
            "data": {
                "videos": return_results
            }

        }
    )

# to get a video with a specific ID
# video_id --> id of video you want to obtain
@app.route("/video/<int:video_id>", methods=["GET"])
def getVideo(video_id):
    result = Video.query.filter_by(id=video_id).first()
    if not result:
        return jsonify(
            {
                "success": False,
                "message": "Video not found"
            }
        )
    formatted_result = video_schema.dump(result)
    return jsonify(
        {
            "success": True,
            "data": {
                "videos": formatted_result
            }

        }
    )

# to post
@app.route("/video", methods=["POST"])
def postVideo():
    try:
        # =======getting the fields based on the request object=======
        name = request.json.get("name")
        likes = request.json.get("likes")
        views = request.json.get("views")
        video = Video(name=name, likes=likes, views=views)
        db.session.add(video)
        db.session.commit()
        return jsonify(
            {
                "success": True,
                "message": "Successfully added",
            }
        )
    except:
        return jsonify(
            {
                "success": False,
                "message":"Failed to add"
            }
        )

# to update
# video_id --> id of the video you intend to update
@app.route("/video/<int:video_id>", methods=["PUT"])
def updateVideo(video_id):
    # =====find whether item exists=====
    result = Video.query.filter_by(id=video_id).first()
    if not result:
        return jsonify(
            {
                "success": False,
                "message": "Video not found; unable to update"
            }
        )
    name = request.args.get("name")
    likes = request.args.get("likes")
    views = request.args.get("views")
    if name:
        result.name = name
    if likes:
        result.likes = likes
    if views:
        result.views = views
    db.session.commit()
    return jsonify(
        {
            "success": True,
            "message": "Successfully updated"
        }
    )


# to delete a specific video
# video_id --> id of video you want to delete
@app.route("/video/<int:video_id>", methods=["DELETE"])
def deleteVideo(video_id):
    targetVideo = Video.query.filter_by(id=video_id).first()
    if not targetVideo:
        return jsonify(
            {
                "success": False,
                "message": "Video not found; unable to delete"
            }
        )
    result = Video.query.filter_by(id=video_id).delete()
    db.session.commit()
    if result:
        return jsonify(
            {
                "success": True,
                "message": "Deletion successful"
            }
        )

# to delete everything (FOR TESTING PURPOSES)
@app.route("/video", methods=["DELETE"])
def deleteAllVideos():
    result = Video.query.delete()
    db.session.commit()
    if result:
        return jsonify(
            {
                "success": True,
                "message": "Deletion successful"
            }
        )
    return jsonify(
        {
            "success": False,
            "message": "Deletion failed"
        }
    )


# =================run the app=================
if __name__ == "__main__":
    app.run(debug=True)
