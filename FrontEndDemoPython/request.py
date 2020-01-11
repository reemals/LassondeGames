import requests
import json


url = ''
# Function checkError is used to print results from requests
# 0 for error found, 1 for error not found, -1 for LocalHost not running
def checkError(result):
    if (result == 'Bad Request'):
        print("Command failed. \n=============\n Bad Request \n=============")
        return -1
    else:
        result_j = result.json()
        type_info = str(result_j['type'])
        print("type: <" + type_info + ">")
        if (type_info != "SUCCESS"):
            errorMessage = result_j['message']
            errorType = result_j['failure']
            print("Command failed: " + errorType + "\n=============\n" + errorMessage + "\n=============")
            return 0
        else:
            return 1

# createInstace sets up the connection with the BackEnd
def createInstance():
    # Check old instance data
    errorExists = checkError(getInstance())
    # If error == -1 -> local host cannot be found
    if (errorExists == -1):
        print('ERROR - Backend Instance Not Running')
        return 'ERROR'
    else:
        if (errorExists == 0):
            deleteinstance()
        r = requests.post('http://localhost:8081/instance')
        if (checkError(r) == 1):
            result = r.json()
            return result
        return 'ERROR'

# Delete instance is used when creating a new instance
# Ensures no previous connections exist
def deleteinstance():
    r = requests.delete('http://localhost:8081/instance')
    checkError(r)
    return r

# Gets the current Instance and all Information
def getInstance():
    try:
        r = requests.get('http://localhost:8081/instance')
    except:
        r = 'Bad Request'
    return r

# Gets a subset of information from the instance
# Note: MapData includes asteroid locations, as well as mars and charging locations
def getData():
    try:
        r = requests.get('http://localhost:8081/instance')
        rjson = r.json()
        result = rjson['payload']
        result['mapData'] = rjson['mapData']
    except:
        result = 'Bad Request'
    return result

# finish needs to be called to check if a successful landing
# on Mars was completed
def finish():
    r = requests.post('http://localhost:8081/finish')
    checkError(r)
    return r

# Turn defines a new direction to spin the Rocket in
# Turning Requires 1 fuel regardless of current orientation
# except if no turn is required (ex. Facing North and turn North)
def turn(direction):
    r = getInstance()
    rjson = r.json()
    facing = str(rjson['payload']['direction'])
    print("facing: {} direction: {}".format(facing, direction))
    if (facing != direction):
        facing = direction
        url = 'http://localhost:8081/turn/' + str(direction)
        r = requests.post(url)
        checkError(r)
        facing_new = getInstance().json()['payload']['direction']
        print("Now facing: " + str(facing_new))
    
# Move the rocket a certain number of spaces
# move(number of times to move)
def move(amount):
    for _ in range(amount):
        r = requests.post('http://localhost:8081/move')
        inst = getInstance().json()
        print("The rocket is at: " + str(inst['payload']['location']))
        error = checkError(r)
        if (error == 0):
            break

# Refuel the rocket at one of the two station locations
# Hint their coordinates are given in the instance data
def refuel():
    r = requests.post('http://localhost:8081/refuel')
    error = checkError(r)
    if error == 1:
        print("The rocket is refueled")
