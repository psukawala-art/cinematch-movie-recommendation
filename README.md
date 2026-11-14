# CineMatch — MySQL Movie Recommendation System

A beginner-friendly student project using MySQL for data, Python for recommendation logic, and Streamlit for the interface.

## Technology
- MySQL: relational database and SQL
- Python: application and recommendation logic
- MySQL Connector/Python: Python-to-MySQL connection
- Streamlit: simple local interface
- unittest: automated checks

## First-version scope
1. Store users, movies, genres, movie-genre links, and ratings.
2. Select a sample user.
3. Recommend movies based on highly rated genres, excluding movies already rated.
4. Add a Linear Algebra extension using rating vectors and cosine similarity.
5. Display recommendations in Streamlit.

This is a learning prototype, not a Netflix clone. It does not include streaming video, payments, or production accounts.

## Four-person team
- Member 1: database schema and ER diagram
- Member 2: sample data and SQL queries
- Member 3: Linear Algebra and recommendation algorithm
- Member 4: Python/MySQL integration and Streamlit
- All members review code and prepare for the viva.

## Setup on Mac
1. Ensure your existing MySQL server is running.
2. Create a virtual environment:
   `python3 -m venv .venv`
   `source .venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run `sql/01_schema.sql`, then `sql/02_sample_data.sql` in MySQL.
5. Copy `.streamlit/secrets.example.toml` to `.streamlit/secrets.toml` and fill in your local credentials.
6. Start the app: `streamlit run app.py`

Never commit `.streamlit/secrets.toml`, passwords, or other secrets.

## Team workflow
Create a GitHub Issue per task. Work on a branch, commit small changes, open a Pull Request, ask a teammate to review, and merge only when it works. Keep `main` runnable.

## SDLC documents
- `docs/requirements.md`
- `docs/design.md`
- `docs/sdlc-plan.md`
- `docs/team-work-plan.md`
- `CHANGELOG.md`

## Tests
Run `python -m unittest discover -s tests -v`.
