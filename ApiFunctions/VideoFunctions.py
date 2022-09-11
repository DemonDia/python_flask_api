from flask import jsonify
from config import db
from Models.Video import *


# ==============Create Operations
# create
def createVideo(jsonObject):
    try:
        # =======getting the fields based on the request object=======
        name = jsonObject.get("name")
        likes = jsonObject.get("likes")
        views = jsonObject.get("views")
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

# =============Read Operations 
# get all videos
def getAllVideos():
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

# get 1 videos
def getVideoById(video_id):
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
# =============Update functions
def updateVideoById(video_id,jsonData):
    # =====find whether item exists=====
    result = Video.query.filter_by(id=video_id).first()
    if not result:
        return jsonify(
            {
                "success": False,
                "message": "Video not found; unable to update"
            }
        )
    name = jsonData.get("name")
    likes = jsonData.get("likes")
    views = jsonData.get("views")
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

# ==========Delete Functions
# delete 1 video
def deleteVideoById(video_id):
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

# delete all videos
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