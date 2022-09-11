from flask import request
from config import app
from ApiFunctions.VideoFunctions import *
from ApiFunctions.UserFunctions import *
# ===========================app routes===========================

# =================Video API routes=================
# to get ALL the videos in the db
@app.route("/video", methods=["GET"])
def getAllForVideo():
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
def deleteAllForVideo():
    return deleteAllVideos()


# =================User API routes=================
@app.route("/user", methods=["GET"])
def getAllForUser():
    return getAllUsers()

# to get a user with a specific ID
# user_id --> id of user you want to obtain
@app.route("/user/<int:user_id>", methods=["GET"])
def getUser(user_id):
    return getUserById(user_id)
# to post
@app.route("/user", methods=["POST"])
def postUser():
    return createUser(request.json)


# to update
# user_id --> id of the user you intend to update
@app.route("/user/<int:user_id>", methods=["PUT"])
def updateUser(user_id):
    return updateUserById(user_id,request.args)

# to delete a specific user
# user_id --> id of user you want to delete
@app.route("/user/<int:user_id>", methods=["DELETE"])
def deleteSingleUser(user_id):
    print("user_id",user_id)
    return deleteUserById(user_id)

# to delete everything (FOR TESTING PURPOSES)
@app.route("/user", methods=["DELETE"])
def deleteAllForUser():
    return deleteAllUsers()


# =================run the app=================
if __name__ == "__main__":
    app.run(debug=True)
