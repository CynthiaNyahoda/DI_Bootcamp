-- Write a query to get the first three characters of each first name of all the employees in the employees table
SELECT SUBSTRING(first_name, 1, 3) FROM employees;