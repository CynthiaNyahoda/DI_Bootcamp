SELECT * FROM Library;

-- select the name of the student and the title of the borrowed books
SELECT s.name, b.title
FROM Student s
JOIN Library l ON s.student_id = l.student_fk_id
JOIN Book b ON b.book_id = l.book_fk_id;

-- select the average age of the children that borrowed the book Alice in Wonderland
SELECT AVG(s.age)
FROM Student s
JOIN Library l ON s.student_id = l.student_fk_id
JOIN Book b ON b.book_id = l.book_fk_id
WHERE b.title = 'Alice In Wonderland';

-- delete a student from the Student table
DELETE FROM Student WHERE name = 'Lera';

-- check what happened in the Library table (since ON DELETE CASCADE is used)
SELECT * FROM Library;




