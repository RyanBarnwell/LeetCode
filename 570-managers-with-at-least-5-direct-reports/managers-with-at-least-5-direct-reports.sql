# Write your MySQL query statement below
Select e2.name
From Employee e1 
    JOIN Employee e2 ON e1.managerID = e2.id
GROUP BY e1.managerId
HAVING COUNT(e1.id) >= 5