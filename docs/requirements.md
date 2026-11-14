# Requirements — CineMatch

## Problem
Viewers can struggle to choose a movie from a large catalogue. CineMatch demonstrates a small, explainable recommendation method based on ratings and genres.

## Users
- Primary: a student/demonstrator selecting a sample user profile.
- Secondary: team members and instructor reviewing the database and queries.

## Goals
- Store movie data in a relational MySQL database.
- Demonstrate keys, joins, filtering, grouping, and aggregation.
- Recommend movies the selected user has not rated.
- Explain recommendations through genre preferences and optionally similar users.
- Demonstrate Linear Algebra through rating vectors and cosine similarity.
- Provide a simple Streamlit interface after core logic works.

## Functional requirements
- FR1: Create users, movies, genres, movie_genres, and ratings tables.
- FR2: Load a documented sample dataset.
- FR3: Retrieve users, movies, ratings, and genres with SQL.
- FR4: Find genres of movies a user rated 4/5 or higher.
- FR5: Exclude movies already rated by the selected user.
- FR6: Return up to five ranked recommendations when candidates exist.
- FR7: Display title, year, genres, and recommendation explanation.
- FR8: Calculate cosine similarity for two rating vectors as the Linear Algebra extension.
- FR9: Handle unknown users, empty results, and database connection errors.

## Non-functional requirements
- Readable code suitable for beginner team members.
- Parameterized SQL values in Python.
- Credentials stored locally and never committed.
- Reproducible sample data and setup instructions.
- Runs locally on a team member's Mac.

## Constraints
- One-week schedule, four beginners, MySQL required by instructor.
- No streaming video, payment, or production account system.
- Do not claim machine learning unless a machine-learning method is implemented and evaluated.

## Acceptance criteria
- [ ] SQL scripts create the schema and load sample data.
- [ ] Five tables and foreign keys exist.
- [ ] Queries return expected records.
- [ ] Recommendations exclude already-rated movies.
- [ ] Empty results do not crash the app.
- [ ] Cosine similarity has a hand-worked example and a code test.
- [ ] README setup instructions work from a clean checkout.
- [ ] All members can explain the project and their own contribution.
