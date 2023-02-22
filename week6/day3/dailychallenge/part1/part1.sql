-- Query 1: The first_name of the LoggedIn customers
SELECT c.first_name
FROM Customer c
JOIN customer_profile cp ON c.id = cp.customer_id
WHERE cp.isLoggedIn = true;

-- Query 2: All the customers first_name and isLoggedIn columns - even the customers those who don’t have a profile.
SELECT c.first_name, cp.isLoggedIn
FROM Customer c
LEFT JOIN customer_profile cp ON c.id = cp.customer_id;

-- Query 3: The number of customers that are not LoggedIn
SELECT COUNT(c.id)
FROM Customer c
LEFT JOIN customer_profile cp ON c.id = cp.customer_id
WHERE cp.id IS NULL OR cp.isLoggedIn = false;




