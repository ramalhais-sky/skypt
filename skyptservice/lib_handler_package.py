import json
import os
import lib_common_auth
import lib_common_http
import lib_common_package
import sys
import requests

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

        ploads = {'token':event['data']['token'],'package':cursor.lastrowid}
        r = requests.get(lib_common_http.endpoints['email']['package'],json=ploads)
        ro = json.loads(r.text)
        if ro["statusCode"]==200:
            response = {
                "statusCode": 200,
                "body": {
                    "package": cursor.lastrowid,
                    "mail": "S"
                }
            }
        else:
            response = {
                "statusCode": 206,
                "body": {
                    "package": cursor.lastrowid,
                    "mail": "F"
                }
            }

    except: # catch *all* exceptions
        e = sys.exc_info()[0]
        response = {
            "statusCode": 400,
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
        cursor = dbcon.cursor(buffered=True, dictionary=True)
        sql = f'SELECT id, user, package from package where id={event["data"]["package"]}'
        cursor.execute(sql)
        package = cursor.fetchone()
        print(package)
        response = {
            "statusCode": 200,
            "body": {
                "package": package
            }
        }
    except:
        e = sys.exc_info()[0]
        response = {
            "statusCode": 400,
            "body": e
        }

    return response
