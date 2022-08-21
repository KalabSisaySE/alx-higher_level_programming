-- creates the database `hbtn_0d_usa` and the table `cities`
-- `id` is unique, auto generated, not null and primary key
-- `states_id` FK references `id` in `states` table

-- create database
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

-- use database
USE `hbtn_0d_usa`;

-- create table
CREATE TABLE IF NOT EXISTS `cities` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `states_id` INT NOT NULL,
    `name` VARCHAR(256) NOT NULL,
    FOREIGN KEY (`states_id`) REFERENCES `states`(`id`)
);
