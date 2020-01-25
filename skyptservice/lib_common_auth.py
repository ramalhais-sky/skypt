import os
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
