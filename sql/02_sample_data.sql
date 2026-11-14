USE cinematch;

INSERT IGNORE INTO users (user_id, name, email) VALUES
(1, 'Param', 'param@example.com'),
(2, 'Aisha', 'aisha@example.com'),
(3, 'Dev', 'dev@example.com'),
(4, 'Riya', 'riya@example.com');

INSERT IGNORE INTO movies (movie_id, title, release_year) VALUES
(1, 'Inception', 2010), (2, 'Interstellar', 2014),
(3, 'The Dark Knight', 2008), (4, 'The Conjuring', 2013),
(5, 'Insidious', 2010), (6, 'Arrival', 2016),
(7, 'Tenet', 2020), (8, 'The Martian', 2015),
(9, 'Shutter Island', 2010);

INSERT IGNORE INTO genres (genre_id, genre_name) VALUES
(1, 'Sci-Fi'), (2, 'Thriller'), (3, 'Action'), (4, 'Horror'),
(5, 'Drama'), (6, 'Adventure'), (7, 'Crime'), (8, 'Mystery');

INSERT IGNORE INTO movie_genres (movie_id, genre_id) VALUES
(1,1), (1,2), (2,1), (2,5), (3,3), (3,7), (4,4), (5,4),
(6,1), (6,5), (7,1), (7,2), (7,3), (8,1), (8,5), (8,6), (9,2), (9,8);

INSERT IGNORE INTO ratings (user_id, movie_id, rating) VALUES
(1,1,5.0), (1,2,5.0), (1,4,2.0),
(2,2,5.0), (2,6,4.0), (2,7,4.0), (2,9,4.0),
(3,4,5.0), (3,5,5.0), (3,9,3.0),
(4,1,4.0), (4,7,5.0), (4,3,4.0), (4,8,4.0);
