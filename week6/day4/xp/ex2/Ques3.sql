-- Write a query to get the all employees whose first_name has both the letters ‘c’ and ‘e’
SELECT * FROM employees WHERE first_name LIKE '%c%' AND first_name LIKE '%e%';