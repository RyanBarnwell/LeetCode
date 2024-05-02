# Write your MySQL query statement below
Select COUNT(DISTINCT user_id) AS active_users, activity_date AS day
From Activity
WHERE activity_date <= "2019/07/27" and activity_date > "2019/06/27"
GROUP BY activity_date