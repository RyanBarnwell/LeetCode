# Write your MySQL query statement below
Select name, bonus
from Employee e
Left Join Bonus b on b.empId = e.empId
where bonus < 1000 or bonus is null