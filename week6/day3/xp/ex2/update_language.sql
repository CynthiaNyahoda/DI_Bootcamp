UPDATE film
SET language_id = (SELECT language_id FROM language WHERE name = 'French')
WHERE title = 'My Movie Title';

