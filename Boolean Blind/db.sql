CREATE DATABASE IF NOT EXISTS ctf_db;
USE ctf_db;

CREATE TABLE flags_bbsqli (
    id INT AUTO_INCREMENT PRIMARY KEY,
    flag VARCHAR(255)
);

INSERT INTO flags_bbsqli (flag) VALUES ('ACS{boolean_bl1nd_sqli_success}');

