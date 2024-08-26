CREATE DATABASE demo;

USE demo;

CREATE TABLE products(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    code VARCHAR(50) NOT NULL UNIQUE,
                    category VARCHAR(100) NOT NULL,
                    size VARCHAR(50) NOT NULL,
                    unit_price DECIMAL(10, 2) NOT NULL,
                    inventory INT NOT NULL,
                    color VARCHAR(255) NOT NULL
) engine=InnoDB default charset = utf8mb4 collate = utf8mb4_general_ci;