# Team Work Plan — Four Beginners

## Member 1 — Schema and ER diagram
Owns: sql/01_schema.sql and docs/erd.md.
Learn: tables, data types, primary/foreign keys, one-to-many and many-to-many relationships.
Deliver: working five-table schema and matching ER diagram.
Review: Member 2 checks sample data against the schema.

## Member 2 — Sample data and SQL queries
Owns: sql/02_sample_data.sql and sql/03_queries.sql.
Learn: INSERT, SELECT, WHERE, JOIN, GROUP BY, AVG, ORDER BY, subqueries.
Deliver: repeatable sample data and tested queries with expected results.
Review: Member 1 checks key consistency.

## Member 3 — Linear Algebra and algorithm
Owns: src/recommender.py and docs/math-example.md.
Learn: vectors, dot product, magnitude, cosine similarity, Python lists/functions.
Deliver: tested similarity function and hand-worked example.
Review: Member 2 checks the rating data assumptions.

## Member 4 — Integration and Streamlit
Owns: src/db.py and app.py.
Learn: Python functions/imports, Connector/Python, Streamlit widgets, error handling.
Deliver: local app that reads from MySQL and displays recommendations.
Review: Member 1 checks setup; Member 3 checks algorithm integration.

## Shared responsibilities
Everyone reviews one teammate's work, writes their own report section, tests their changes, and prepares for the viva.

Suggested branches:
- docs/requirements-and-sdlc
- feature/mysql-schema
- feature/sample-data-queries
- feature/recommender
- feature/streamlit-integration

Use short-lived branches and avoid editing the same file simultaneously.
