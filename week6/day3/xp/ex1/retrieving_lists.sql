-- Retrieve a list of all films joined with their languages, including films with no languages
SELECT f.title, f.description, fl.language
FROM Films f
LEFT JOIN FilmLanguages fl ON f.id = fl.film_id

UNION

-- Retrieve a list of all languages, even if there are no films in those languages
SELECT null AS title, null AS description, l.language
FROM (
  SELECT DISTINCT language FROM FilmLanguages
) l
LEFT JOIN FilmLanguages fl ON l.language = fl.language
LEFT JOIN Films f ON fl.film_id = f.id
WHERE f.id IS NULL;
