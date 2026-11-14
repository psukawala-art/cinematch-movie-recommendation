USE cinematch;

-- List all movies
SELECT movie_id, title, release_year FROM movies ORDER BY title;

-- Show ratings with user and movie names
SELECT u.name, m.title, r.rating
FROM ratings AS r
JOIN users AS u ON u.user_id = r.user_id
JOIN movies AS m ON m.movie_id = r.movie_id
ORDER BY u.name, m.title;

-- Average rating per movie
SELECT m.title, ROUND(AVG(r.rating), 2) AS average_rating, COUNT(*) AS number_of_ratings
FROM movies AS m
JOIN ratings AS r ON r.movie_id = m.movie_id
GROUP BY m.movie_id, m.title
ORDER BY average_rating DESC;

-- Movies a user has not rated; replace 1 with another user_id
SELECT m.movie_id, m.title
FROM movies AS m
WHERE NOT EXISTS (
    SELECT 1 FROM ratings AS r
    WHERE r.movie_id = m.movie_id AND r.user_id = 1
)
ORDER BY m.title;

-- Genres from movies a user rated 4 or higher
SELECT DISTINCT g.genre_name
FROM ratings AS r
JOIN movie_genres AS mg ON mg.movie_id = r.movie_id
JOIN genres AS g ON g.genre_id = mg.genre_id
WHERE r.user_id = 1 AND r.rating >= 4.0;
