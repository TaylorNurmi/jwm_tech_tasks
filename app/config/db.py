import logging
import sqlite3
from datetime import datetime

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        create_table(conn)
    except sqlite3.Error:
        logging.exception("Error connecting to database")
    return conn

def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            birth_date TEXT NOT NULL,
            courses TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """)
        conn.commit()
    except sqlite3.Error:
        logging.exception("Error creating table")

def get_row_by_id(conn, id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id = ?", (id,))
    return cursor.fetchone()

def insert_row(conn, data):
    try:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO students (name, birth_date, courses, created_at, updated_at) 
        VALUES (?, ?, ?, ?, ?)
        """, (
            data["name"], 
            data["birth_date"], 
            data["courses"], 
            datetime.now().isoformat(),
            datetime.now().isoformat()
        ))
        conn.commit()
    except sqlite3.Error:
        logging.exception("Error inserting row")
