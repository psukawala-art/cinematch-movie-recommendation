import mysql.connector
import streamlit as st


def fetch_all(sql, params=()):
    # Run a parameterized SELECT using local Streamlit secrets.
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(**st.secrets["mysql"])
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql, params)
        return cursor.fetchall()
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
