-- Write a query which will find the 10 cheapest movies.
SELECT film_id, title, description, rental_rate FROM film ORDER BY rental_rate ASC LIMIT 10
