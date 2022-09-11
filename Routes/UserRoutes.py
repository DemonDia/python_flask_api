from config import app
from flask import request
from ApiFunctions.UserFunctions import *

# to get ALL the users in the db
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