-- This file prepares MySQL server

CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;
CREATE USER IF NOT EXISTS hbn_test@localhost IDENTI_FIED BY 'hbnb_test_pwd';
GRANT ALL PREVILEGE ON hbnb_test_db.* TO hbnb_test@localhost;
GRANT SELECT ON performance_schema.* TO hbnb_test@localhost;