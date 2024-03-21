-- DATABASE setup
-- USEr setup
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY "hbnb_dev_pwd";
GRANT SELECT ON perfomance_schema.* TO 'hbnb_dev'@'localhost';
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
