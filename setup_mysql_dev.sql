-- DATABASE setup
-- USEr setup
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY "hbnb_dev_pwd";
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
USE hbnb_dev_db;
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
USE mysql;
GRANT SELECT ON perfomance_schema.* TO 'hbnb_dev'@'localhost';
