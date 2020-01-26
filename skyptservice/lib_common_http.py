endpoints = {
    "email": {
        "package": 'http://skypt-email-package:8080/email/package'
    },
    "package": {
        "get": 'http://skypt-package-get:8080/package/get'
    },
    "employee": {
        "getbyuser": 'http://skypt-employee-getbyuser:8080/employee/getbyuser'
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