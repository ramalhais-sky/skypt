import os

env_token = os.environ['skypt_token']

def validateToken(requestdata):
    if 'data' not in requestdata.keys():
        return getErrorResponse()
        
    if 'token' not in requestdata['data'].keys():
        return getErrorResponse()
    
    if (requestdata['data']['token']!=env_token):
        return getErrorResponse()

    return 0

def getErrorResponse():
    return {
        "statusCode": 401,
        "body": "Invalid token"
    }