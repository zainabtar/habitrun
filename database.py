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

# This function shall add 5 predefined habits if the database is empty.
def add_default_habits():
    habits = get_all_habits()

    # Only add habits if there are none yet
    if len(habits) == 0:
        add_habit("Drink Water", "Drink 2L of water", "daily")
        add_habit("Exercise", "Do a short workout", "daily")
        add_habit("Read", "Read 10 pages", "daily")
        add_habit("Call Family", "Make a weekly call", "weekly")
        add_habit("Clean Room", "Clean the room once a week", "weekly")

def get_completions_for_habit(habit_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT completed_at FROM completions
        WHERE habit_id = ?
        ORDER BY completed_at
    """, (habit_id,))

    results = cursor.fetchall()

    conn.close()

    # Extract timestamps into a list
    completions = []
    for row in results:
        completions.append(row[0])

    return completions
