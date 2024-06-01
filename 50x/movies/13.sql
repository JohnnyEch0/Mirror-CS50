SELECT name from people JOIN stars ON people.id = stars.person_id WHERE stars.movie_id IN (
    SELECT id FROM movies JOIN stars on movies.id = stars.movie_id WHERE stars.person_id IN (
        SELECT id FROM people WHERE name = 'Kevin Bacon' AND birth = 1958
    )
) AND NOT stars.person_id IN (
    SELECT id FROM stars JOIN people on stars.person_id = people.id WHERE people.name = 'Kevin Bacon'
);



