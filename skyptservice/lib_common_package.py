import os
import mysql.connector
import lib_common_http

env_dbhost = os.environ['skypt_dbhost']
env_dbuser = os.environ['skypt_dbuser']
env_dbpass = os.environ['skypt_dbpass']
env_dbdatabase = os.environ['skypt_dbdatabase']

def dbcon():
    db = mysql.connector.connect(
        host=f'{env_dbhost}',
        user=env_dbuser,
        passwd=env_dbpass,
        database=env_dbdatabase
    )
    db.autocommit = True
    return db


def validateAddPackageRequest(requestdata):
    if 'data' not in requestdata.keys():
        return lib_common_http.getBadRequestErrorResponse()

    if 'user' not in requestdata['data'].keys():
        return lib_common_http.getBadRequestErrorResponse()

    if 'package' not in requestdata['data'].keys():
        return lib_common_http.getBadRequestErrorResponse()

    return 0

def validateGetPackageRequest(requestdata):
    if 'data' not in requestdata.keys():
        return lib_common_http.getBadRequestErrorResponse()

    if 'package' not in requestdata['data'].keys():
        return lib_common_http.getBadRequestErrorResponse()

    return 0

# TODO: use python schema package to validate response
def validateGetPackageResponse(responsedata):
    if 'body' not in responsedata.keys():
        return lib_common_http.getBadRequestErrorResponse()

    if 'package' not in responsedata['body'].keys():
        return lib_common_http.getBadRequestErrorResponse()

    if 'id' not in responsedata['body']['package'].keys():
        return lib_common_http.getBadRequestErrorResponse()

    if 'user' not in responsedata['body']['package'].keys():
        return lib_common_http.getBadRequestErrorResponse()

    if 'package' not in responsedata['body']['package'].keys():
        return lib_common_http.getBadRequestErrorResponse()

    return 0
