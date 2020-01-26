import lib_common_http

def getPropertyValue(data,key):
    if key in data.keys():
        return str(data[key][0],'utf-8')
    else:
        return ""

# TODO: use python schema package to validate dictionary
def validateGetByNameRequest(requestdata):
    if 'data' not in requestdata.keys():
        return lib_common_http.getBadRequestErrorResponse()
        
    if 'name' not in requestdata['data'].keys():
        return lib_common_http.getBadRequestErrorResponse()

    return 0

# TODO: use python schema package to validate dictionary
def validateGetByUserRequest(requestdata):
    if 'data' not in requestdata.keys():
        return lib_common_http.getBadRequestErrorResponse()
        
    if 'user' not in requestdata['data'].keys():
        return lib_common_http.getBadRequestErrorResponse()

    return 0