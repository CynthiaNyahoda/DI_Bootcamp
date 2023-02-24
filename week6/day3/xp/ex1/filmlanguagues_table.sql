-- Create a Films table
CREATE TABLE Films (
  id INT PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
  title VARCHAR(255) NOT NULL,
  description TEXT
);

-- Create a FilmLanguages table to store the language(s) of each film
CREATE TABLE FilmLanguages (
  film_id INT NOT NULL,
  language VARCHAR(255) NOT NULL,
  FOREIGN KEY (film_id) REFERENCES Films(id) ON DELETE CASCADE
);

