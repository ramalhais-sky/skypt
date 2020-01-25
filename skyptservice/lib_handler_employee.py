import json
import ldap
import os

import lib_common

env_ldapnode = os.environ['skypt_ldapnode']
env_ldapuser = os.environ['skypt_ldapuser']
env_ldappass = os.environ['skypt_ldappass']
env_ldapbase = os.environ['skypt_ldapbase']

con = ldap.initialize(f'ldap://{env_ldapnode}')
con.simple_bind_s(env_ldapuser,env_ldappass)
ldap_base = env_ldapbase

def getValue(data,key):
    if key in data.keys():
        return data[key][0]
    else:
        return ""

def getByName(event, context):
    resp = lib_common.validateToken(event)
    if resp!=0:
        return resp

    query = f"(& (objectclass=user) (cn=*{event['data']['name'].replace(' ','*')}*))"
    result = con.search_s(ldap_base, ldap.SCOPE_SUBTREE, query)
    results = []
    for dn, user in result:
        x = {
            "cn": getValue(user,"cn"),
            "user": getValue(user,"sAMAccountName"),
            "email": getValue(user,"mail"),
            "mobile": getValue(user,"mobile")
        }
        results.append(x)

    body = {
        "total": len(results),
        "employees": results
    }

    response = {
        "statusCode": 200,
        "body": str(body).replace(": b'",": '")
    }

    return response

# Local test set environment vars
# export skypt_ldapnode=
# export skypt_ldapuser=
# export skypt_ldappass=''
# export skypt_ldapbase=''
# export skypt_token =
# print(json.dumps(getByName({"data":{"token":"xxx","name":"Doe"}}, '')))
