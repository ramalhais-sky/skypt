import json
import os
import lib_common_auth
import lib_common_package
import sys

dbcon = lib_common_package.dbcon()

def add(event, context):
    resp = lib_common_auth.validateToken(event)
    if resp!=0:
        return resp

    resp = lib_common_package.validateAddPackageRequest(event)
    if resp!=0:
        return resp

    try:
        cursor = dbcon.cursor()
        sql = "INSERT INTO package (user, package) VALUES (%s, %s)"
        val = (event['data']['user'], event['data']['package'])
        cursor.execute(sql, val)
        dbcon.commit()
        response = {
            "statusCode": 200,
            "body": f'Record inserted {cursor.rowcount}'
        }

    except: # catch *all* exceptions
        e = sys.exc_info()[0]
        response = {
            "statusCode": 400,
            "body": f'{e}'
        }

    return response

# Local test set environment vars
# export skypt_ldapnode=
# export skypt_ldapuser=
# export skypt_ldappass=''
# export skypt_ldapbase=''
# export skypt_token =
# print(json.dumps(getByName({"data":{"token":"xxx","name":"Doe"}}, '')))
