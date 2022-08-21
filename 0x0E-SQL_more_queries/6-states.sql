-- creates the database `hbtn_0d_usa` and the table `states`
-- id is unique auto generated, and primary key

-- create database
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

-- use database
USE `hbtn_0d_usa`;

-- create table
CREATE TABLE IF NOT EXISTS `states` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(256) 
);
