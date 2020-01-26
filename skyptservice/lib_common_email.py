import lib_common_http

def validatePackageRequest(requestdata):
    if 'data' not in requestdata.keys():
        return lib_common_http.getBadRequestErrorResponse()
        
    if 'package' not in requestdata['data'].keys():
        return lib_common_http.getBadRequestErrorResponse()

    return 0