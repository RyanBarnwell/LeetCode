# Write your MySQL query statement below
#month() doesn't work for this problem
SELECT DATE_FORMAT(trans_date, "%Y-%m") AS month, country,
    COUNT(DISTINCT id) AS trans_count, 
    COUNT(DISTINCT case when state = 'approved' then id else null end) AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(case when state = 'approved' then amount else 0 end) AS approved_total_amount
FROM Transactions
GROUP BY month, country