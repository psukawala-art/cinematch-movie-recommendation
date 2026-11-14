# Design — CineMatch

## Architecture
Streamlit UI → Python functions → MySQL Connector/Python → MySQL database.
The recommendation module receives rating data, calculates scores, and returns ranked results to the UI.

## Data model
- users(user_id PK, name, email)
- movies(movie_id PK, title, release_year)
- genres(genre_id PK, genre_name)
- movie_genres(movie_id PK/FK, genre_id PK/FK)
- ratings(user_id PK/FK, movie_id PK/FK, rating, rated_at)

A user can rate many movies; a movie can receive ratings from many users. Movies and genres have a many-to-many relationship resolved by movie_genres.

For the prototype, a recorded rating is treated as evidence the user has seen the movie. This avoids a separate watch-history table.

## Components
- sql/01_schema.sql: database and table definitions
- sql/02_sample_data.sql: deterministic sample dataset
- sql/03_queries.sql: SQL practice and query examples
- src/db.py: database connection helper
- src/recommender.py: pure recommendation and similarity functions
- app.py: Streamlit interface
- tests/: automated tests

## Recommendation approach
Version 1: identify genres from movies rated 4/5 or higher, exclude already-rated titles, and rank candidates using available ratings. Label this as rule-based.

Linear Algebra extension: represent users as rating vectors over movies both users rated. Calculate cosine similarity:
cos(A, B) = (A · B) / (||A|| ||B||)

Missing ratings mean unknown, not zero. Handle zero vectors safely.

## Error handling
- Friendly message when MySQL is unavailable.
- Parameterized SQL values.
- Empty recommendation list when no candidates exist.
- Do not reveal passwords in errors.
- Close database cursors and connections reliably.

## Security
Credentials belong in local .streamlit/secrets.toml. Commit only the example file. Use a dedicated database account rather than root where possible.
