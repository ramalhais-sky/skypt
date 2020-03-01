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
    
    pkg = {}
    usr = {}

    # Get Package
    try:
        ploads = {'token':event['data']['token'],'package':event['data']['package']}
        r = requests.get(lib_common_http.endpoints['package']['get'],json=ploads)
        ro = json.loads(r.text)
        print("Email_GetPackage",ro)
        if ro["statusCode"]==200:
            resp = lib_common_package.validateGetPackageResponse(ro)
            if resp!=0:
                return resp
            else:
                pkg = ro["body"]["package"]
        else:
            return lib_common_http.getNotFoundErrorResponse()
    except Exception as e:
        print("Email_GetPackage_ERROR",ploads)
        return {
            "statusCode": 400,
            "body": e
        }
    
    # Get User
    try:
        ploads = {'token':event['data']['token'],'user':pkg['user']}
        r = requests.get(lib_common_http.endpoints['employee']['getbyuser'],json=ploads)
        ro = json.loads(r.text)
        print("Email_GetUser",ro)
        if ro["statusCode"]==200:
            resp = lib_common_employee.validateGetByUserResponse(ro)
            if resp!=0:
                return resp
            else:
                usr = ro["body"]["employees"][0]
        else:
            return lib_common_http.getNotFoundErrorResponse()
    except Exception as e:
        print("Email_GetUser_ERROR",ploads)
        return {
            "statusCode": 454,
            "body": e
        }

    # Build and send mail
    resp = lib_common_email.sendPackageMail({"pkg":pkg,"usr":usr})
    
    if resp == 0:
        response =  {
            "statusCode": 200,
            "body": "Message sent"
        }
    else:
        response =  {
            "statusCode": 484,
            "body": resp
        }

    return response
