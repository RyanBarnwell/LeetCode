# Write your MySQL query statement below
Select product_name, year, price
From Product
Inner Join Sales on Sales.product_id = Product.product_id