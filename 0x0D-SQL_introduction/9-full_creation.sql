-- Script to create a table second_table in the database hbtn_0c_0 and add multiple rows
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Inserting records into second_table
INSERT INTO second_table (id, name, score) VALUES (1, 'John', 10); -- Inserting John
INSERT INTO second_table (id, name, score) VALUES (2, 'Alex', 3);  -- Inserting Alex
INSERT INTO second_table (id, name, score) VALUES (3, 'Bob', 14);  -- Inserting Bob
INSERT INTO second_table (id, name, score) VALUES (4, 'George', 8); -- Inserting George
