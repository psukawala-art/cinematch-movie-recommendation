import streamlit as st
from mysql.connector import Error
from src.db import fetch_all

st.set_page_config(page_title="CineMatch", page_icon="🎬", layout="wide")
st.title("🎬 CineMatch")
st.caption("A student-built MySQL movie recommendation prototype")

try:
    users = fetch_all("SELECT user_id, name FROM users ORDER BY name")
except Exception:
    st.error("Could not connect to MySQL. Check that MySQL is running and local secrets are correct.")
    st.stop()

if not users:
    st.info("No users found. Run the SQL setup and sample-data scripts first.")
    st.stop()

user = st.selectbox("Choose a user", users, format_func=lambda item: item["name"])

if st.button("Recommend movies", type="primary"):
    sql = '''
    SELECT m.movie_id, m.title, m.release_year,
           GROUP_CONCAT(DISTINCT g.genre_name ORDER BY g.genre_name SEPARATOR ', ') AS genres,
           ROUND(AVG(r.rating), 2) AS average_rating,
           COUNT(DISTINCT r.user_id) AS rating_count
    FROM movies AS m
    JOIN movie_genres AS mg ON mg.movie_id = m.movie_id
    JOIN genres AS g ON g.genre_id = mg.genre_id
    JOIN ratings AS r ON r.movie_id = m.movie_id
    WHERE EXISTS (
        SELECT 1
        FROM movie_genres AS liked_mg
        WHERE liked_mg.movie_id = m.movie_id
          AND liked_mg.genre_id IN (
              SELECT mg2.genre_id
              FROM ratings AS my_ratings
              JOIN movie_genres AS mg2 ON mg2.movie_id = my_ratings.movie_id
              WHERE my_ratings.user_id = %s AND my_ratings.rating >= 4.0
          )
    )
    AND NOT EXISTS (
        SELECT 1 FROM ratings AS seen
        WHERE seen.user_id = %s AND seen.movie_id = m.movie_id
    )
    GROUP BY m.movie_id, m.title, m.release_year
    ORDER BY average_rating DESC, rating_count DESC, m.title
    LIMIT 5
    '''
    try:
        results = fetch_all(sql, (user["user_id"], user["user_id"]))
    except Error:
        st.error("The recommendation query failed. Check the schema and SQL setup.")
        st.stop()

    if results:
        st.subheader(f"Recommendations for {user['name']}")
        st.caption("Rule-based suggestions from genres of movies rated 4/5 or higher; already-rated movies are excluded.")
        st.dataframe(results, use_container_width=True, hide_index=True)
    else:
        st.info("No recommendations found for this user in the current sample data.")
