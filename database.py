# database.py
# File handles SQLite database setup and data storage.

import sqlite3

DB_NAME = "habits.db"


def initialize_database():
    """Create database tables if they do not already exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS habits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            periodicity TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS completions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            habit_id INTEGER NOT NULL,
            completed_at TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def add_habit(name, description, periodicity):
    """Add a new habit to the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO habits (name, description, periodicity)
        VALUES (?, ?, ?)
    """, (name, description, periodicity))

    conn.commit()
    conn.close()


def get_all_habits():
    """Return all habits from the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM habits")
    habits = cursor.fetchall()

    conn.close()
    return habits


def check_off_habit(habit_id, completed_at):
    """Save a completion event for a habit."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO completions (habit_id, completed_at)
        VALUES (?, ?)
    """, (habit_id, completed_at))

    conn.commit()
    conn.close()


def add_default_habits():
    """Add predefined habits if the database is empty."""
    habits = get_all_habits()

    if len(habits) == 0:
        add_habit("Drink Water", "Drink 2L of water", "daily")
        add_habit("Exercise", "Do a short workout", "daily")
        add_habit("Read", "Read 10 pages", "daily")
        add_habit("Call Family", "Make a weekly call", "weekly")
        add_habit("Clean Room", "Clean the room once a week", "weekly")


def get_completions_for_habit(habit_id):
    """Return all completion timestamps for one habit."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT completed_at FROM completions
        WHERE habit_id = ?
        ORDER BY completed_at
    """, (habit_id,))

    results = cursor.fetchall()
    conn.close()

    completions = []
    for row in results:
        completions.append(row[0])

    return completions
