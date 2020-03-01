import json
import os
import lib_common_auth
import lib_common_http
import lib_common_package
import sys
import requests

dbcon = lib_common_package.dbcon()

def add(event, context):
    print("PackageAddRequest",event, context)
    resp = lib_common_auth.validateToken(event)
    if resp!=0:
        return resp

    print(event)

    resp = lib_common_package.validateAddPackageRequest(event)
    if resp!=0:
        return resp

    try:
        dbcon.ping(reconnect=True, attempts=3, delay=5)
        cursor = dbcon.cursor()
        sql = "INSERT INTO package (user, package) VALUES (%s, %s)"
        val = (event['data']['user'], event['data']['package'])
        cursor.execute(sql, val)
        package = cursor.lastrowid

        ploads = {'token':event['data']['token'],'package':cursor.lastrowid}
        r = requests.get(lib_common_http.endpoints['email']['package'],json=ploads)
        ro = json.loads(r.text)
        print("EmailPackage",ro)
        if ro["statusCode"]==200:
            response = {
                "statusCode": 200,
                "body": {
                    "package": package,
                    "mail": "S",
                    "data": ro['body']
                }
            }
        else:
            response = {
                "statusCode": 206,
                "body": {
                    "package": package,
                    "mail": "F",
                    "data": ro['body']
                }
            }

    except: # catch *all* exceptions
        print("ERROR",ploads)
        e = sys.exc_info()[0]
        response = {
            "statusCode": 423,
            "body": e
        }

    return response

def get(event, context):
    resp = lib_common_auth.validateToken(event)
    if resp!=0:
        return resp

    resp = lib_common_package.validateGetPackageRequest(event)
    if resp!=0:
        return resp
    try:
        dbcon.ping(reconnect=True, attempts=3, delay=5)
        cursor = dbcon.cursor(dictionary=True)
        sql = f'SELECT id, user, package, unix_timestamp(created) as date from package where id={event["data"]["package"]}'
        cursor.execute(sql)
        package = cursor.fetchone()
        print("GetPackageOrigin",package)
        if len(package)>0:
            response = {
                "statusCode": 200,
                "body": {
                    "package": package
                }
            }
        else:
            return lib_common_http.getNotFoundErrorResponse()
    except:
        e = sys.exc_info()[0]
        response = {
            "statusCode": 424,
            "body": e
        }

    return response
