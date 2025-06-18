CREATE DATABASE ctf_sqli1;
USE ctf_sqli1;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(50)
);

INSERT INTO users (username, password) VALUES
('bob', 'bobpass'),
('robert', 'robertpass'),
('rose', 'rosepass'),
('caesar', 'caesarpass'),
('admin', 'adminpass');

CREATE TABLE messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sender VARCHAR(50),
    recipient VARCHAR(50),
    content TEXT
);

INSERT INTO messages (sender, recipient, content) VALUES
('caesar', 'rose', 'The treasure is under the oak tree. synt{lbh_sbhaq_gur_frperg}');
