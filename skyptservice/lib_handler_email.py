import json
import requests
import lib_common_http
import lib_common_auth
import lib_common_email
import lib_common_package

def package(event, context):

    resp = lib_common_auth.validateToken(event)
    if resp!=0:
        return resp

    resp = lib_common_email.validatePackageRequest(event)
    if resp!=0:
        return resp

    ploads = {'token':event['data']['token'],'package':event['data']['package']}
    r = requests.get(lib_common_http.endpoints['package']['get'],json=ploads)
    ro = json.loads(r.text)

    if ro["statusCode"]==200:
        resp = lib_common_package.validateGetPackageResponse(ro)
        if resp!=0:
            response = resp
        else:
            response = {
                "statusCode": 200,
                "body": ro
            }
    else:
        response = lib_common_http.getNotFoundErrorResponse()

    return response
