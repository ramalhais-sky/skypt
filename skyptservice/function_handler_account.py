import json
import lib_common_auth

def createPackage(event, context):
    user,resp = lib_common_auth.getBasicAuthUser(event)
    if resp!=0:
        return resp

    response = {
        "statusCode": 200,
        "body": user
    }
    return response

def listPackages(event, context):
    user,resp = lib_common_auth.getBasicAuthUser(event)
    if resp!=0:
        return resp

    response = {
        "statusCode": 200,
        "body": user
    }
    return response
