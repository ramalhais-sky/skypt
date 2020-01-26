endpoints = {
    "email": {
        "package": 'http://skypt-email-package:8080/email/package'
    },
    "package": {
        "get": 'http://skypt-package-get:8080/package/get'
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