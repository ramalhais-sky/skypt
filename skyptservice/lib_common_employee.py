import lib_common_http

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