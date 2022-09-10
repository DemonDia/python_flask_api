import requests

# base URL
BASE = "http://127.0.0.1:5000/"

# =============================Helper functions=============================

# generate test data
def generateData(dataSize):
    for i in range(1, dataSize+1):
        req = requests.post(BASE+"video", json={
            "name": "Video  #{i}".format(i=i),
            "likes": 100 * i,
            "views": 10000 * i
        })

# emptys database
def deleteAll():
    requests.delete(BASE+"video")

# back to defaults
def resetToDefaults(dataSize):
    deleteAll()
    generateData(dataSize)

# =========CRUD helpers=========
# =====Create=====
# add video
# videoJson --> a json object containing data of video to be INSERTED
def addVideo(videoJson):
    addedVideo = requests.post(BASE+"video", json=videoJson)
    return addedVideo.json()



# =====Read=====
# get a specific video
def getVideo(videoId):
    obtainVideo = requests.get(BASE+"video/{videoId}".format(videoId=videoId))
    return obtainVideo.json()

# get all videos
def getAllVideos():
    videos = requests.get(BASE+"video")
    return videos.json()


# =====Update=====
# update a specific video
# videoId --> id of a video you intend to update
# videoJson --> a json object containing data of video to be UPDATED
def updateVideo(videoId,videoJson):
    updatedVideo = requests.put(BASE+"video/{videoId}".format(videoId=videoId),params = videoJson)
    return updatedVideo.json()

# =====Delete=====
# delete a specific video
# videoId --> id of a video you intend to delete

def deleteVideo(videoId):
    deletedVideo = requests.delete(
        BASE+"video/{videoId}".format(videoId=videoId))
    return deletedVideo.json()


# =============================Different types of requests=============================
# ====================GET request====================
# Get ALL data: response = requests.get(BASE+"route")
# id --> id of item you intend to get
# Get data with given ID: response = requests.get(BASE+"route/{id}".format(id =id))

# ====================POST request====================
# parsed_data --> data is to be in json format
# Post data: response = requests.post(BASE+"route",json=parsed_data)

# ====================PUT request====================
# This means UPDATE
# id --> id of item you intend to update
# parsed_data --> data is to be in json format (you update with these values)
# Update data: response = requests.post(BASE+"route/{id}".format(id=id),json=parsed_data)


# ====================DELETE request====================
# id --> id of item you intend to delete
# Delete data: response = requests.delete(BASE+"route/{id}".format(id=id))


# ========================================Test cases========================================

# ====================Test Case 1: Get all Data(With contents)====================
def testCase1():
    print("=============+Test Case 1=============+")
    print(getAllVideos())
    print()

# ====================Test Case 2: Get all Data(Without contents)====================


def testCase2():
    print("=============+Test Case 2=============+")
    deleteAll()
    print(getAllVideos())
    print()
    resetToDefaults(25)

# ====================Test Case 3: Get Data with Specified ID(Pass)====================


def testCase3():
    print("=============+Test Case 3=============+")
    print(getVideo(12))
    print()

# ====================Test Case 4: Get Data with Specified ID(fail)====================


def testCase4():
    print("=============+Test Case 4=============+")
    print(getVideo(122))
    print()

# ====================Test Case 5: Add Data(Pass)====================


def testCase5():
    print("=============+Test Case 5=============+")
    videoJson = {
        "name": "random video",
        "likes": 250000,
        "views": 450000000
    }
    print(addVideo(videoJson))
    print()

# ====================Test Case 6: Add Data(Fail)====================


def testCase6():
    print("=============+Test Case 6=============+")

    print("========a)Missing name========")
    videoJsonA = {
        "likes": 18287,
        "views": 22727276
    }
    print(addVideo(videoJsonA))
    print()

    print("========b)Missing likes========")
    videoJsonB = {
        "name": "random video X",
        "views": 400080
    }
    print(addVideo(videoJsonB))
    print()

    print("========c)Missing views========")
    videoJsonC = {
        "name": "random video 3",
        "likes": 250000,
    }
    print(addVideo(videoJsonC))
    print()
    print()


# ====================Test Case 7: Update Data(Pass)====================


def testCase7():
    print("=============+Test Case 7=============+")
    print("========Original Object========")
    print(getVideo(12))
    print()

    print("========a)Change Name========")
    videoJsonA={
        "name": "DJ Fest"
    }
    print(updateVideo(12,videoJsonA))
    print(getVideo(12))
    print()

    print("========b)Change Views========")
    videoJsonB={
        "views": 12000
    }
    print(updateVideo(12,videoJsonB))
    print(getVideo(12))
    print()

    print("========c)Change Likes========")
    videoJsonC={
        "likes": 482
    }
    print(updateVideo(12,videoJsonC))
    print(getVideo(12))
    print()

    print("========d)Change All========")
    videoJsonD={
        "name": "Rock Performance",
        "views": 6000000,
        "likes": 83373
    }
    print(updateVideo(12,videoJsonD))
    print(getVideo(12))
    print()
    print()


# ====================Test Case 8: Update Data(Fail)====================


def testCase8():
    print("=============+Test Case 8=============+")

    print("========Target Object(Before)========")
    print(getVideo(12))
    print()

    print("========a)id is big========")
    videoJsonA={
        "name": "Cat Dancing",
        "views": 49545442,
        "likes": 65785
    }
    print(updateVideo(1111,videoJsonA))
    print()
    print("========b)id is negative========")
    videoJsonB={
        "name": "Cat Dancing",
        "views": 49545442,
        "likes": 65785
    }
    print(updateVideo(1111,videoJsonB))
    print()

    print("========Target Object(After)========")
    print(getVideo(12))
    print()
# ====================Test Case 9: Delete Data(Pass)====================


def testCase9():
    print("=============+Test Case 9=============+")
    print("========Before Deleting========")
    print(getVideo(13))
    print()

    print(deleteVideo(13))
    print()

    print("========After Deleting========")
    print(getVideo(13))
    print()
    print()

# ====================Test Case 10: Delete Data(Fail)====================


def testCase10():
    print("=============+Test Case 10=============+")
    print("========Before Deleting========")
    print(getVideo(222))
    print()

    print(deleteVideo(222))
    print()

    print("========After Deleting========")
    print(getVideo(222))
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
