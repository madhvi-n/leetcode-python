# Write your MySQL query statement below
# SELECT c.name as Customers FROM Customers as c 
# LEFT JOIN Orders as o 
# ON c.id = o.customerId 
# WHERE o.id IS NULL;

SELECT name AS Customers FROM customers WHERE id NOT IN (SELECT customerId FROM Orders);
