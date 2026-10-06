CREATE DATABASE Demo;

USE demo;

CREATE TABLE users (
    id INT PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    created_at CURRENT_TIMESTAMP
);

INSERT INTO users (name, email) VALUES ("Alice", "Alice@example.com");

SELECT * FROM users;