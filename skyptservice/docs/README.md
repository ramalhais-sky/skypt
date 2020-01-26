## Build a runtime
https://github.com/kubeless/runtimes
```
docker build -t python_ldap . -f Dockerfile.3.7
docker tag python_ldap:latest freedomson/python_ldap:latest
docker push freedomson/python_ldap:latest
```

## Kubeless runtime update helpers
```
kubectl edit configmap kubeless-config -n kubeless
```
```
kubectl scale deployments.apps kubeless-controller-manager -n kubeless --replicas=1
```
```
kubectl get pods -n kubeless
```
```
kubeless get-server-config
```
```
kubectl logs -n kubeless -l kubeless=controller -c kubeless-function-controller
```
```
kubeless function call employee-getbyname --data '{"token":"xxx","name":"Doe John"}'
```
