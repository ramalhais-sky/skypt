import json
import lib_common_auth
import lib_common_email

def package(event, context):

    resp = lib_common_auth.validateToken(event)
    if resp!=0:
        return resp

    resp = lib_common_email.validatePackageRequest(event)
    if resp!=0:
        return resp

    response = {
        "statusCode": 200,
        "body": f'Email sent'
    }

    return response
