import json
import requests
import lib_common_http
import lib_common_auth
import lib_common_email
import lib_common_package
import lib_common_employee

def package(event, context):

    resp = lib_common_auth.validateToken(event)
    if resp!=0:
        return resp

    resp = lib_common_email.validatePackageRequest(event)
    if resp!=0:
        return resp

    # Get Package
    try:
        ploads = {'token':event['data']['token'],'package':event['data']['package']}
        r = requests.get(lib_common_http.endpoints['package']['get'],json=ploads)
        ro = json.loads(r.text)
        pkg = {}
        if ro["statusCode"]==200:
            resp = lib_common_package.validateGetPackageResponse(ro)
            if resp!=0:
                return resp
            else:
                pkg = ro["body"]["package"]
        else:
            return lib_common_http.getNotFoundErrorResponse()
    except Exception as e:
        return {
            "statusCode": 400,
            "body": e
        }
    
    # Get User
    try:
        ploads = {'token':event['data']['token'],'user':pkg['user']}
        r = requests.get(lib_common_http.endpoints['employee']['getbyuser'],json=ploads)
        ro = json.loads(r.text)
        user = {}
        if ro["statusCode"]==200:
            resp = lib_common_employee.validateGetByUserResponse(ro)
            if resp!=0:
                return resp
            else:
                user = ro["body"]["employees"][0]
                return {
                    "statusCode": 200,
                    "body": {
                        "package": pkg,
                        "user": user
                    }
                }
        else:
            return lib_common_http.getNotFoundErrorResponse()
    except Exception as e:
        return {
            "statusCode": 400,
            "body": e
        }

    return response
