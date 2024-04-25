# Write your MySQL query statement below
Select w1.id
#2 weather instances
From Weather w1, Weather w2
#temp is greater
where w1.temperature > w2.temperature
#difference in dates = 1, only compare to previous
and DATEDIFF(w1.recordDate, w2.recordDate) = 1