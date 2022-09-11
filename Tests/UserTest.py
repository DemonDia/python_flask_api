import requests

# base URL
BASE = "http://127.0.0.1:5000/user"

# =============================Helper functions=============================

# generate test data
def generateData(dataSize):
    for i in range(1, dataSize+1):
        req = requests.post(BASE, json={
            "name": "User  #{i}".format(i=i)
        })

# emptys database
def deleteAll():
    requests.delete(BASE)

# back to defaults
def resetToDefaults(dataSize):
    deleteAll()
    generateData(dataSize)

# =========CRUD helpers=========
# =====Create=====
# add user
# userJson --> a json object containing data of user to be INSERTED
def addUser(userJson):
    addedUser = requests.post(BASE, json=userJson)
    return addedUser.json()



# =====Read=====
# get a specific user
def getUser(userId):
    obtainUser = requests.get(BASE+"/{userId}".format(userId=userId))
    return obtainUser.json()

# get all users
def getAllUsers():
    users = requests.get(BASE)
    return users.json()


# =====Update=====
# update a specific user
# userId --> id of a user you intend to update
# userJson --> a json object containing data of user to be UPDATED
def updateUser(userId,userJson):
    updatedUser = requests.put(BASE+"/{userId}".format(userId=userId),params = userJson)
    return updatedUser.json()

# =====Delete=====
# delete a specific user
# userId --> id of a user you intend to delete

def deleteUser(userId):
    deletedUser = requests.delete(
        BASE+"/{userId}".format(userId=userId))
    return deletedUser.json()


# =============================Different types of requests=============================
# ====================GET request====================
# Get ALL data: response = requests.get(BASE)
# id --> id of item you intend to get
# Get data with given ID: response = requests.get(BASE+"/{id}".format(id =id))

# ====================POST request====================
# parsed_data --> data is to be in json format
# Post data: response = requests.post(BASE,json=parsed_data)

# ====================PUT request====================
# This means UPDATE
# id --> id of item you intend to update
# parsed_data --> data is to be in json format (you update with these values)
# Update data: response = requests.post(BASE+"/{id}".format(id=id),json=parsed_data)


# ====================DELETE request====================
# id --> id of item you intend to delete
# Delete data: response = requests.delete(BASE+"/{id}".format(id=id))


# ========================================Test cases========================================

# ====================Test Case 1: Get all Data(With contents)====================
def testCase1():
    print("=============Test Case 1: Get all Data(With contents)=============+")
    print(getAllUsers())
    print()

# ====================Test Case 2: Get all Data(Without contents)====================


def testCase2():
    print("=============Test Case 2: Get all Data(Without contents)=============+")
    deleteAll()
    print(getAllUsers())
    print()
    resetToDefaults(25)

# ====================Test Case 3: Get Data with Specified ID(Pass)====================


def testCase3():
    print("=============Test Case 3: Get Data with Specified ID(Pass)=============+")
    print(getUser(12))
    print()

# ====================Test Case 4: Get Data with Specified ID(fail)====================


def testCase4():
    print("=============Test Case 4: Get Data with Specified ID(fail)=============+")
    print(getUser(122))
    print()

# ====================Test Case 5: Add Data(Pass)====================


def testCase5():
    print("=============Test Case 5: Add Data(Pass)=============+")
    userJson = {
        "name": "random user",
    }
    print(addUser(userJson))
    print()

# ====================Test Case 6: Add Data(Fail)====================


def testCase6():
    print("=============Test Case 6: Add Data(Fail)=============+")
    userJsonA = {

    }
    print(addUser(userJsonA))
    print()
    print()


# ====================Test Case 7: Update Data(Pass)====================


def testCase7():
    print("=============Test Case 7: Update Data(Pass)=============+")
    print("========Original Object========")
    print(getUser(12))
    print()

    print("========a)Change Name========")
    userJsonA={
        "name": "DJ Fest"
    }
    print(updateUser(12,userJsonA))
    print(getUser(12))
    print()

    print("========b)Change Views========")
    userJsonB={
        "views": 12000
    }
    print(updateUser(12,userJsonB))
    print(getUser(12))
    print()

    print("========c)Change Likes========")
    userJsonC={
        "likes": 482
    }
    print(updateUser(12,userJsonC))
    print(getUser(12))
    print()

    print("========d)Change All========")
    userJsonD={
        "name": "Rock Performance",
        "views": 6000000,
        "likes": 83373
    }
    print(updateUser(12,userJsonD))
    print(getUser(12))
    print()
    print()


# ====================Test Case 8: Update Data(Fail)====================


def testCase8():
    print("=============Test Case 8: Update Data(Fail)=============+")

    print("========Target Object(Before)========")
    print(getUser(12))
    print()

    print("========a)id is big========")
    userJsonA={
        "name": "Shimizu Esora",

    }
    print(updateUser(1111,userJsonA))
    print()
    print("========b)id is negative========")
    userJsonB={
        "name": "Yor Forger"
    }
    print(updateUser(1111,userJsonB))
    print()

    print("========Target Object(After)========")
    print(getUser(12))
    print()
# ====================Test Case 9: Delete Data(Pass)====================


def testCase9():
    print("=============Test Case 9: Delete Data(Pass=============+")
    print("========Before Deleting========")
    print(getUser(13))
    print()

    print(deleteUser(13))
    print()

    print("========After Deleting========")
    print(getUser(13))
    print()
    print()

# ====================Test Case 10: Delete Data(Fail)====================


def testCase10():
    print("=============Test Case 10: Delete Data(Fail)=============")
    print("========Before Deleting========")
    print(getUser(222))
    print()

    print(deleteUser(222))
    print()

    print("========After Deleting========")
    print(getUser(222))
    print()
    print()

# ====================Master test function====================


def main():
    # initialise
    resetToDefaults(25)
    # test commence
    testCase1()
    testCase2()
    testCase3()
    testCase4()
    testCase5()
    testCase6()
    testCase7()
    testCase8()
    testCase9()
    testCase10()

    return


if (__name__ == "__main__"):
    main()
