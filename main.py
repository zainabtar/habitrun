from datetime import datetime
import database

# Make sure the database exists before the menu starts
database.initialize_database()


def show_menu():
    print("\n=== HabitRun ===")
    print("1. Create a habit")
    print("2. View all habits")
    print("3. Check off a habit")
    print("4. Exit")


while True:
    show_menu()
    choice = input("Choose an option: ")

    # Option 1: create a habit
    if choice == "1":
        name = input("Enter habit name: ")
        description = input("Enter habit description: ")
        periodicity = input("Enter periodicity (daily/weekly): ")

        database.add_habit(name, description, periodicity)
        print("Habit added successfully.")

    # Option 2: show all the habits
    elif choice == "2":
        habits = database.get_all_habits()

        if len(habits) == 0:
            print("No habits found.")
        else:
            print("\nTracked Habits:")
            for habit in habits:
                print(habit)

    # Option 3: habit marked as completed
    elif choice == "3":
        habit_id = input("Enter habit ID to check off: ")
        completed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        database.check_off_habit(habit_id, completed_at)
        print("Habit checked off successfully.")

    # Option 4: exit the program
    elif choice == "4":
        print("Goodbye!")
        break

    # other choice is Invalid
    else:
        print("Invalid option. Please try again.")
