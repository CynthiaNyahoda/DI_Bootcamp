-- Write a query to display the last names of all employees whose last name contains exactly six characters.
SELECT last_name FROM employees WHERE LENGTH(last_name) = 6;