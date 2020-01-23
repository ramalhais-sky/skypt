Dependencies:
Kubeless
Serverless
npm

Install:
serverless deploy

getuser request:
```
curl -X GET \
  http://10.79.123.102/getuser \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 82cfb952-5d17-4645-a59f-e9372ce482ce' \
  -H 'cache-control: no-cache' \
  -H 'host: skypt.dev.hhe.nonprod.imp.sky.com' \
  -d '{"username":"ramalhais"}'
```

getuser response:
```
{"statusCode": 200, "body": "{'total': 1, 'employees': [{'cn': 'Ramalhais, Pedro', 'user': 'PXXX', 'email': 'pedro.xxx@xxx', 'mobile': '+351xxxxxx'}]}"}
```

Kubeless runtime update helpers:
kubectl edit configmap kubeless-config -n kubeless
kubectl scale deployments.apps kubeless-controller-manager -n kubeless --replicas=1
kubectl get pods -n kubeless
kubeless get-server-config
kubectl logs   -n kubeless -l kubeless=controller -c kubeless-function-controller
kubeless function call getuser --data '{"username":"Albemarle"}