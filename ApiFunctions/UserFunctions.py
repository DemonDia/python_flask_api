from flask import jsonify
from config import db
from Models.User import *

# ==============Create Operations==============
# create
def createUser(jsonObject):
    try:
        # =======getting the fields based on the request object=======
        name = jsonObject.get("name")
        user = User(name=name)
        db.session.add(user)
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

# =============Read Operations==============
# get all users
def getAllUsers():
    result = User.query.all()
    return_results = users_schema.dump(result)
    # results = [i.tojson() for i in result]
    return jsonify(
        {
            "success": True,
            "data": {
                "users": return_results
            }

        }
    )

# get 1 user
def getUserById(user_id):
    result = User.query.filter_by(id=user_id).first()
    if not result:
        return jsonify(
            {
                "success": False,
                "message": "User not found"
            }
        )
    formatted_result = user_schema.dump(result)
    return jsonify(
        {
            "success": True,
            "data": {
                "users": formatted_result
            }

        }
    )
# =============Update functions==============
def updateUserById(user_id,jsonData):
    # =====find whether item exists=====
    result = User.query.filter_by(id=user_id).first()
    if not result:
        return jsonify(
            {
                "success": False,
                "message": "User not found; unable to update"
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

# ==========Delete Functions==============
# delete 1 user
def deleteUserById(user_id):
    targetUser = User.query.filter_by(id=user_id).first()
    if not targetUser:
        return jsonify(
            {
                "success": False,
                "message": "User not found; unable to delete"
            }
        )
    result = User.query.filter_by(id=user_id).delete()
    db.session.commit()
    if result:
        return jsonify(
            {
                "success": True,
                "message": "Deletion successful"
            }
        )

# delete all users
def deleteAllUsers():
    result = User.query.delete()
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