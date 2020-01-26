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
  -d '{"token":"xxx","email":"john.doe@xxx.com","package":"data:image/gif;base64,R0lGODlh..."}'
```

#### Success response body
```
{
    "statusCode": 200,
    "body": "Record inserted 1"
}
```

#### Error response body
```
{
    "statusCode": 401,
    "body": "Invalid token"
}
{
    "statusCode": 400,
    "body": "Bad request"
}
```

### /package/get
```
curl -X GET \
  https://10.79.123.102/package/get \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 1c183088-9665-4f57-a174-8b7b1fd7fa2b' \
  -H 'cache-control: no-cache' \
  -H 'host: skypt.dev.hhe.nonprod.imp.sky.com' \
  -d '{"token":"xxx","package":"129"}'
```

#### Success response body
```
{
    "statusCode": 200,
    "body": {
        "package": {
            "id": 129,
            "user": "xpto31",
            "package": "data:image/gif;base64,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"
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
  -d '{"token":"xxx","name":"John Doe"}'
```

#### Success response body
```
{
    "statusCode": 200,
    "body": "{'total': 1, 'employees': [{'cn': 'Doe, John', 'user': '', 'email': '', 'mobile': ''}]}"
}
```

#### Error response body
```
{
    "statusCode": 401,
    "body": "Invalid token"
}
{
    "statusCode": 400,
    "body": "Bad request"
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
