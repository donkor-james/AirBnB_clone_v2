-- Creates MySQL server with database hbnb_dev_db
-- And previleges for new user

-- Creates database if it doesn't exist
CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;

--create User hbnb_dev if not exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grants all privileges on hbnb_dev_db to hbnb_dev
GRANT ALL PREVILEGE ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

--Grants SELECT privileges on performance schema to hbnb_dev
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';

-- Flush privileges to applied changes
Flush PREVILEGE;
