# main.py
# This file runs the HabitRun application through a simple CLI menu.

from datetime import datetime
import database
import analysis

# Create the database tables if they do not already exist
database.initialize_database()

# Add predefined habits if the database is empty
database.add_default_habits()


def show_menu():
    """Display the main menu."""
    print("\n=== HabitRun ===")
    print("1. Create a habit")
    print("2. View all habits")
    print("3. Check off a habit")
    print("4. Show all habit names")
    print("5. Show habits by periodicity")
    print("6. Show longest streak for a habit")
    print("7. Exit")


while True:
    show_menu()
    choice = input("Choose an option: ")

    # Option 1: create a new habit
    if choice == "1":
        name = input("Enter habit name: ")
        description = input("Enter habit description: ")
        periodicity = input("Enter periodicity (daily/weekly): ").lower()

        if periodicity not in ["daily", "weekly"]:
            print("Invalid periodicity. Please enter 'daily' or 'weekly'.")
        else:
            database.add_habit(name, description, periodicity)
            print("Habit added successfully.")

    # Option 2: show all saved habits
    elif choice == "2":
        habits = database.get_all_habits()

        if len(habits) == 0:
            print("No habits found.")
        else:
            print("\nTracked Habits:")
            for habit in habits:
                print(habit)

    # Option 3: mark a habit as completed
    elif choice == "3":
        try:
            habit_id = int(input("Enter habit ID to check off: "))
            completed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            database.check_off_habit(habit_id, completed_at)
            print("Habit checked off successfully.")
        except ValueError:
            print("Please enter a valid numeric habit ID.")

    # Option 4: show all habit names
    elif choice == "4":
        names = analysis.get_all_habit_names()

        if len(names) == 0:
            print("No habits found.")
        else:
            print("\nHabit Names:")
            for name in names:
                print(name)

    # Option 5: filter habits by periodicity
    elif choice == "5":
        periodicity = input("Enter periodicity (daily/weekly): ").lower()
        habits = analysis.get_habits_by_periodicity(periodicity)

        if len(habits) == 0:
            print("No habits found.")
        else:
            print("\nFiltered Habits:")
            for habit in habits:
                print(habit)

    # Option 6: show longest streak for one habit
    elif choice == "6":
        try:
            habit_id = int(input("Enter habit ID: "))
            streak = analysis.get_longest_streak_for_habit(habit_id)
            print("Longest streak:", streak)
        except ValueError:
            print("Please enter a valid numeric habit ID.")

    # Option 7: exit
    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")
