SELECT film.title, COUNT(*) AS rental_count, SUM(payment.amount) AS total_revenue
FROM film
JOIN inventory ON film.film_id = inventory.film_id
JOIN rental ON inventory.inventory_id = rental.inventory_id
JOIN payment ON rental.rental_id = payment.rental_id
WHERE rental.return_date IS NULL
GROUP BY film.title
ORDER BY total_revenue DESC
LIMIT 30;
