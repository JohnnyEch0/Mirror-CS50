SELECT COUNT(title) FROM Movies WHERE id IN (SELECT movie_id FROM ratings WHERE rating = 10.0);
