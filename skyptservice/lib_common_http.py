endpoints = {
    "email": {
        "package": 'http://skyptemailpackage:8080/emailpackage'
    },
    "package": {
        "get": 'http://skyptpackageget:8080/packageget'
    },
    "employee": {
        "getbyuser": 'http://skyptemployeegetbyuser:8080/employeegetbyuser'
    }
}

def getAuthErrorResponse():
    return {
        "statusCode": 401,
        "body": "Invalid token"
    }

def getBadRequestErrorResponse():
    return {
        "statusCode": 400,
        "body": "Bad request"
    }

def getNotFoundErrorResponse():
    return {
        "statusCode": 404,
        "body": "Not found"
    }