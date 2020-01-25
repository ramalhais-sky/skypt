CREATE DATABASE `imp-skypt`;
CREATE TABLE package (
    id int NOT NULL AUTO_INCREMENT,
    email varchar(255),
    package LONGTEXT,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);