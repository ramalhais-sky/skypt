endpoint_email_package = 'http://skypt-email-package:8080/email/package'

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
