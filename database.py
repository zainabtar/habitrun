import sqlite3

# This is a function that creates the database tables if not existing already.
def initialize_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # creating table to store habit
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


# This function saves new habit into the habits table.
def add_habit(name, description, periodicity):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO habits (name, description, periodicity)
        VALUES (?, ?, ?)
    """, (name, description, periodicity))

    conn.commit()
    conn.close()


# This function gets all the habits from the database.
def get_all_habits():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM habits")
    habits = cursor.fetchall()

    conn.close()
    return habits


# This function will save a completion event for a habit.
def check_off_habit(habit_id, completed_at):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO completions (habit_id, completed_at)
        VALUES (?, ?)
    """, (habit_id, completed_at))

    conn.commit()
    conn.close()
