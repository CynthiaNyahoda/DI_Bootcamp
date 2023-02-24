-- Not satisfied with the results. Write a query which will find the next 10 cheapest movies.
-- Bonus: Try to not use LIMIT.
SELECT film_id, title, description, rental_rate FROM film WHERE film_id NOT IN (SELECT DISTINCT inventory.film_id FROM inventory);