## Dependencies:
* Kubeless
* Serverless
* npm

## Install:
serverless deploy

# Endpoints

## Package

### /package/add
```
curl -X GET \
  https://10.79.123.102/package/add \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -H 'host: skypt.dev.hhe.nonprod.imp.sky.com' \
  -d '{"token":"xxx","user":"xpto31","package":"data:image/gif;base64,R0lGODlh..."}'
```
```
{
    "statusCode": 200,
    "body": {
        "package": 130,
        "mail": "S" // S (sent) // F (failed)
    }
}
```

### /package/get
```
curl -X GET \
  https://10.79.123.102/package/get \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -H 'host: skypt.dev.hhe.nonprod.imp.sky.com' \
  -d '{"token":"xxx","package":"129"}'
```
```
{
    "statusCode": 200,
    "body": {
        "package": {
            "id": 129,
            "user": "xpto31",
            "package": "data:image/gif;base64,R0lGODlh..."
        }
    }
}
```

## Employee

### /employee/getbyname
```
curl -X GET \
  https://10.79.123.102/employee/getbyname \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -H 'host: skypt.dev.hhe.nonprod.imp.sky.com' \
  -d '{"token":"xxx","name":"Doe John"}'
```
```
{
    "statusCode": 200,
    "body": {
        "total": 1,
        "employees": [
            {
                "cn": "Doe, John",
                "user": "xxx",
                "email": "xxx@xxx.xxx",
                "mobile": "+xxx"
            }
        ]
    }
}
```

### /employee/getbyuser
```
curl -X GET \
  https://10.79.123.102/employee/getbyname \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -H 'host: skypt.dev.hhe.nonprod.imp.sky.com' \
  -d '{"token":"xxx","user":"xpto31"}'
```
```
{
    "statusCode": 200,
    "body": {
        "total": 1,
        "employees": [
            {
                "cn": "xxx",
                "user": "xpto31",
                "email": "xxx@xxx.xxx",
                "mobile": "+xxx"
            }
        ]
    }
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
    user varchar(255),
    package LONGTEXT,
    email VARCHAR(1),
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);
```
**User:** 
CREATE USER 'username'@'%' IDENTIFIED BY 'password';
GRANT ALL privileges ON \`database\`.* TO 'username'@'%';

**Sample data:**
```
MariaDB [imp-skypt]> select * from package;
+----+------+-------------+---------------------+---------------------+
| id | user | package     | created             | updated             |
+----+------+-------------+---------------------+---------------------+
|  5 | user | imagebase64 | 2020-01-25 21:45:39 | 2020-01-25 21:45:39 |
+----+------+-------------+---------------------+---------------------+
```

## Build a runtime
https://github.com/kubeless/runtimes
```
cd docs
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
