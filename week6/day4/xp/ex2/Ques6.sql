-- Write a query to display the last name of all employees who have the letter āeā as the third character in the name.
SELECT last_name FROM employees WHERE last_name LIKE '__e%';