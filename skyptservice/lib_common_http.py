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
