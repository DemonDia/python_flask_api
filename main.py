from flask import request
from config import app
from ApiFunctions.VideoFunctions import getVideoById, getAllVideos,createVideo, updateVideoById, deleteVideoById,deleteAllVideos
# =================app routes=================

# to get ALL the videos in the db
@app.route("/video", methods=["GET"])
def getAll():
    return getAllVideos()
# to get a video with a specific ID
# video_id --> id of video you want to obtain
@app.route("/video/<int:video_id>", methods=["GET"])
def getVideo(video_id):
    return getVideoById(video_id)
# to post
@app.route("/video", methods=["POST"])
def postVideo():
    return createVideo(request.json)


# to update
# video_id --> id of the video you intend to update
@app.route("/video/<int:video_id>", methods=["PUT"])
def updateVideo(video_id):
    return updateVideoById(video_id,request.args)

# to delete a specific video
# video_id --> id of video you want to delete
@app.route("/video/<int:video_id>", methods=["DELETE"])
def deleteSingleVideo(video_id):
    return deleteVideoById(video_id)
# to delete everything (FOR TESTING PURPOSES)
@app.route("/video", methods=["DELETE"])
def deleteAll():
    return deleteAllVideos()


# =================run the app=================
if __name__ == "__main__":
    app.run(debug=True)
