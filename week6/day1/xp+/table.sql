CREATE TABLE students (
  id INT PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
  last_name VARCHAR(50),
  first_name VARCHAR(50),
  birth_date DATE
);