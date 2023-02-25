-- Write a query to get the first name, last name and the length of the full name of all the employees from the employees table.
SELECT first_name, last_name, LENGTH(CONCAT(first_name, ' ', last_name)) AS Full_Name_Length FROM employees;
