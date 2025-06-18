CREATE DATABASE ctf_db;
USE ctf_db;

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
);

INSERT INTO products (name) VALUES ('Keyboard'), ('Mouse'), ('Monitor');

CREATE TABLE admin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    secret VARCHAR(255)
);

INSERT INTO admin (secret) VALUES ('ACS{union_sql_injection_success}');
