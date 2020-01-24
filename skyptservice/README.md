## Dependencies:
* Kubeless
* Serverless
* npm

## Install:
serverless deploy

### /employee/getbyname
```
curl -X GET \
  https://10.79.123.102/employee/getbyname \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -H 'host: skypt.dev.hhe.nonprod.imp.sky.com' \
  -d '{"token":"772FDCDA27C4572D141E27B3E21E5","username":"dave"}'
```

#### Response:
```
{"statusCode": 200, "body": "{'total': 1, 'employees': [{'cn': 'Ramalhais, Pedro', 'user': 'PXXX', 'email': 'pedro.xxx@xxx', 'mobile': '+351xxxxxx'}]}"}
```
\
\
\
**Kubeless runtime update helpers:** \
kubectl edit configmap kubeless-config -n kubeless \
kubectl scale deployments.apps \
kubeless-controller-manager -n kubeless --replicas=1 \
kubectl get pods -n kubeless \
kubeless get-server-config \
kubectl logs -n kubeless -l kubeless=controller -c kubeless-function-controller \
kubeless function call getuser --data '{"username":"Albemarle"}