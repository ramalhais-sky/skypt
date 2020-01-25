## Dependencies:
* Kubeless
* Serverless
* npm

## Install:
serverless deploy

## Endpoints

### /employee/getbyname
```
curl -X GET \
  https://10.79.123.102/employee/getbyname \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -H 'host: skypt.dev.hhe.nonprod.imp.sky.com' \
  -d '{"token":"772FDCDA27C4572D141E27B3E21E5","name":"almeida philip"}'
```

#### Success response body
```
{
    "statusCode": 200,
    "body": "{'total': 1, 'employees': [{'cn': 'Almeida, Philip', 'user': '', 'email': '', 'mobile': ''}]}"
}
```
#### Error response body
```
{
    "statusCode": 401,
    "body": "Invalid token"
}
```

## Database
**Cluster:**
```
imp-galera-cluster01-test
```
**Database:**
```
CREATE DATABASE `imp-skypt`;
```
**Tables:** 
```
CREATE TABLE package (
    id int NOT NULL AUTO_INCREMENT,
    email varchar(255),
    package LONGTEXT,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);
```
**Sample data:**
```
MariaDB [imp-skypt]> select * from package;
+----+----------------+-------------------------------+---------------------+---------------------+
| id | email          | package                       | created             | updated             |
+----+----------------+-------------------------------+---------------------+---------------------+
|  5 | philip@now.com | data:image/png;base64,iVBO... | 2020-01-25 00:51:08 | 2020-01-25 00:51:08 |
+----+----------------+-------------------------------+---------------------+---------------------+
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
kubeless function call getuser --data '{"username":"Albemarle"}
```