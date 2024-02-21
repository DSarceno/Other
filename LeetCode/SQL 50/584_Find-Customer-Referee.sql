/*
SQL Scheme:
CREATE TABLE IF NOT EXISTS Customer (id INT, name VARCHAR(25), referee_id INT);
DELETE FROM Customer;
INSERT INTO Customer (id, name, referee_id) VALUES (1, 'Will', NULL);
INSERT INTO Customer (id, name, referee_id) VALUES (2, 'Jane', NULL);
INSERT INTO Customer (id, name, referee_id) VALUES (3, 'Alex', 2);
INSERT INTO Customer (id, name, referee_id) VALUES (4, 'Bill', NULL);
INSERT INTO Customer (id, name, referee_id) VALUES (5, 'Zack', 1);
INSERT INTO Customer (id, name, referee_id) VALUES (6, 'Mark', 2);


Table: Customer

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| referee_id  | int     |
+-------------+---------+
In SQL, id is the primary key column for this table.
Each row of this table indicates the id of a customer, their name, and the id of the customer who referred them.
 

Find the names of the customer that are not referred by the customer with id = 2.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Customer table:
+----+------+------------+
| id | name | referee_id |
+----+------+------------+
| 1  | Will | null       |
| 2  | Jane | null       |
| 3  | Alex | 2          |
| 4  | Bill | null       |
| 5  | Zack | 1          |
| 6  | Mark | 2          |
+----+------+------------+
Output: 
+------+
| name |
+------+
| Will |
| Jane |
| Bill |
| Zack |
+------+
*/


-- SOLUTION
SELECT c.name 
FROM Customer AS c
LEFT JOIN Customer AS cref ON c.referee_id = cref.id
WHERE cref.id IS NULL OR cref.id <> 2