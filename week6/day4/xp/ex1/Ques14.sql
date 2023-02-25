-- Write a query to check whether the first_name column of the employees table contains any numbers.
SELECT * FROM employees WHERE first_name REGEXP '[0-9]'