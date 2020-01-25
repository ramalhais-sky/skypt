import lib_common_http

def validateGetByNameRequest(requestdata):
    if 'data' not in requestdata.keys():
        return lib_common_http.getBadRequestErrorResponse()
        
    if 'name' not in requestdata['data'].keys():
        return lib_common_http.getBadRequestErrorResponse()

    return 0