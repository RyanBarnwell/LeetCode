# Write your MySQL query statement below
Select distinct author_id AS id
From Views
where viewer_id = author_id
Order by author_id ASC