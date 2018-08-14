.read lab12.sql

-- Q5
CREATE TABLE greatstudents AS
  SELECT a.date, a.color, a.pet, b.pet, a.number, b.number FROM students AS a, sp18students AS b WHERE a.date = b.date and a.color = b.color;

-- Q6
CREATE TABLE sevens AS
  SELECT a.seven from students AS a, checkboxes AS b WHERE a.time = b.time and a.number = 7 and b.'7' = 'True';

-- Q7
CREATE TABLE sp18favnum AS
  SELECT number, COUNT(*) FROM sp18students GROUP BY number ORDER BY COUNT(*) DESC LIMIT 1;


CREATE TABLE sp18favpets AS
  SELECT pet, COUNT(*) FROM sp18students GROUP BY pet ORDER BY COUNT(*) DESC LIMIT 10;


CREATE TABLE su18favpets AS
  SELECT pet, COUNT(*) FROM students GROUP BY pet ORDER BY COUNT(*) DESC LIMIT 10;


CREATE TABLE su18dog AS
  SELECT pet, COUNT(*) FROM students WHERE pet = 'dog';


CREATE TABLE su18alldogs AS
  SELECT pet, COUNT(*) FROM students WHERE pet LIKE '%dog%';


CREATE TABLE obedienceimages AS
  SELECT seven, denero, COUNT(*) FROM students WHERE seven = '7' GROUP BY denero;

-- Q8
CREATE TABLE smallest_int_count AS
  SELECT smallest, COUNT(*) FROM students GROUP BY smallest;
