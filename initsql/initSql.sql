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


INSERT INTO products (name, code, category, size, unit_price, inventory, color)
VALUES ('Star', 'A-001', 'cloth', 'S, M', 200.00, 20, 'Red, Blue'),
       ('Moon', 'A-002', 'cloth', 'M, L', 300.00, 10, 'Red, White'),
       ('Eagle', 'B-001', 'pants', 'M, L', 100.00, 23, 'Green'),
       ('Bird', 'B-002', 'pants', 'S, M, L', 50.00, 12, 'Black');