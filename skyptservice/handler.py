import json
import ldap

con = ldap.initialize('ldap://xxx.xxx.com')
con.simple_bind_s("philip.xxx@xxx","xxx")
ldap_base = "OU=xxx,OU=xxs,dc=xxx,dc=com"

def getuser(event, context):

    query = f"(& (objectclass=user) (cn=*{event['data']['username']}*))"
    result = con.search_s(ldap_base, ldap.SCOPE_SUBTREE, query)
    results = []
    for dn, entry in result:
        try:
            m = entry['mobile'][0]
        except:
            x = {
                "cn": entry['cn'][0],
                "user": entry['sAMAccountName'][0],
                "email": entry['mail'][0],
                "mobile": ""
            }
        else:
            x = {
                "cn": entry['cn'][0],
                "user": entry['sAMAccountName'][0],
                "email": entry['mail'][0],
                "mobile": entry['mobile'][0]
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

#print(json.dumps(getuser({"data":{"username":'ramalhais'}}, '')))