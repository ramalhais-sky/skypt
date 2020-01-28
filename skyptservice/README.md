## Dependencies:
* Kubeless
* Serverless
* npm

## Install:
npm install
serverless deploy

# Endpoints

## Package

### /package/add
```
curl -k -X GET \
  https://skypt.lisbongames.com/package/add \
  -H 'Content-Type: application/json' \
  -d '{"token":"xxx","user":"pal31","package":"data:image/gif;base64,R0lGODlhPQBEAPeoAJo..."}'
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
curl -k -X GET \
  https://skypt.lisbongames.com/package/get \
  -H 'Content-Type: application/json' \
  -d '{"token":"xxx","package":"920"}'
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
curl -k -X GET \
  https://skypt.lisbongames.com/employee/getbyname \
  -H 'Content-Type: application/json' \
  -d '{"token":"xxx","name":"almeida philip"}'
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
curl -k -X GET \
  https://skypt.lisbongames.com/employee/getbyuser \
  -H 'Content-Type: application/json' \
  -d '{"token":"xxx","user":"pal31"}'
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
+----+-------+----------------------------------------------+-------+---------------------+---------------------+
| id | user  | package                                      | email | created             | updated             |
+----+-------+----------------------------------------------+-------+---------------------+---------------------+
|  4 | pal31 | data:image/gif;base64,R0lGODlhPQBEAPeoAJo... | P     | 2020-01-27 22:13:24 | 2020-01-27 22:13:24 |
+----+-------+----------------------------------------------+-------+---------------------+---------------------+
```
