-- test database setup
-- USEr setup
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY "hbnb_test_pwd";
GRANT SELECT ON perfomance_schema.* TO 'hbnb_test'@'localhost';
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
