# Write your MySQL query statement below
WITH total_users AS (
    SELECT COUNT(DISTINCT user_id) AS total
    FROM Users
)
SELECT DISTINCT
    contest_id, 
    ROUND(COUNT(user_id) OVER(PARTITION BY contest_id) * 100.0/total, 2) AS percentage
FROM Register, total_users
#GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC