import json
import ldap
import os

env_ldapnode = os.environ['skypt_ldapnode']
env_ldapuser = os.environ['skypt_ldapuser']
env_ldappass = os.environ['skypt_ldappass']
env_ldapbase = os.environ['skypt_ldapbase']

con = ldap.initialize("ldap://"+env_ldapnode)
con.simple_bind_s(env_ldapuser,env_ldappass)
ldap_base = env_ldapbase

def getValue(data,key):
    if key in data.keys():
        return data[key][0]
    else:
        return ""

def getuser(event, context):

    query = f"(& (objectclass=user) (cn=*{event['data']['username'].replace(' ','*')}*))"
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
# print(json.dumps(getuser({"data":{"username":'dave'}}, '')))
