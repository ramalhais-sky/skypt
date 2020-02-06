import os
import base64
import re

import lib_common_http

env_token = os.environ['skypt_token']

def validateToken(requestdata):
    if 'data' not in requestdata.keys():
        return lib_common_http.getBadRequestErrorResponse()
        
    if 'token' not in requestdata['data'].keys():
        return lib_common_http.getBadRequestErrorResponse()
    
    if (requestdata['data']['token']!=env_token):
        return lib_common_http.getAuthErrorResponse()

    return 0

def getBasicAuthUser(event):
    authheader = event['extensions']['request'].get_header('AUTHORIZATION')
    if authheader:
        b64data = re.sub("Basic ", "", authheader)
        decodeddata = base64.b64decode(b64data.encode("ASCII"))
        user,passphrase = decodeddata.decode().split(":", 1)
        return user,0
    return False,lib_common_http.getAuthErrorResponse()
