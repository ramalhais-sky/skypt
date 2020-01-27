import json
import ldap
import os

import lib_common_auth
import lib_common_employee

env_ldapnode = os.environ['skypt_ldapnode']
env_ldapuser = os.environ['skypt_ldapuser']
env_ldappass = os.environ['skypt_ldappass']
env_ldapbase = os.environ['skypt_ldapbase']

def getByName(event, context):
    resp = lib_common_auth.validateToken(event)
    if resp!=0:
        return resp

    resp = lib_common_employee.validateGetByNameRequest(event)
    if resp!=0:
        return resp

    try:
        con = ldap.initialize(f'ldap://{env_ldapnode}')
        con.simple_bind_s(env_ldapuser,env_ldappass)
        ldap_base = env_ldapbase
        query = f"(& (objectclass=user) (cn=*{event['data']['name'].replace(' ','*')}*))"
        result = con.search_s(ldap_base, ldap.SCOPE_SUBTREE, query)
        con.unbind_s()
        results = []
        for dn, user in result:
            x = {
                "cn": lib_common_employee.getPropertyValue(user,"cn"),
                "user": lib_common_employee.getPropertyValue(user,"sAMAccountName"),
                "email": lib_common_employee.getPropertyValue(user,"mail"),
                "mobile": lib_common_employee.getPropertyValue(user,"mobile")
            }
            results.append(x)

        response = {
            "statusCode": 200,
            "body": {
                "total": len(results),
                "employees": results
            }
        }
    except Exception as e:
        response = {
            "statusCode": 404,
            "body": e
        }

    return response

def getByUser(event, context):
    resp = lib_common_auth.validateToken(event)
    if resp!=0:
        return resp

    resp = lib_common_employee.validateGetByUserRequest(event)
    if resp!=0:
        return resp
        
    try:
        con = ldap.initialize(f'ldap://{env_ldapnode}')
        con.simple_bind_s(env_ldapuser,env_ldappass)
        ldap_base = env_ldapbase
        query = f"(& (objectclass=user) (sAMAccountName={event['data']['user']}))"
        result = con.search_s(ldap_base, ldap.SCOPE_SUBTREE, query)
        con.unbind_s()
        results = []
        for dn, user in result:
            x = {
                "cn": lib_common_employee.getPropertyValue(user,"cn"),
                "user": lib_common_employee.getPropertyValue(user,"sAMAccountName"),
                "email": lib_common_employee.getPropertyValue(user,"mail"),
                "mobile": lib_common_employee.getPropertyValue(user,"mobile")
            }
            results.append(x)
            print(x)
        response = {
            "statusCode": 200,
            "body": {
                "total": len(results),
                "employees": results
            }
        }
    except Exception as e:
        response = {
            "statusCode": 404,
            "body": e
        }

    return response
