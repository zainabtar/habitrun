import database


# Function displays all created habits
def get_all_habit_names():
    habits = database.get_all_habits()
    names = []

    for habit in habits:
        names.append(habit[1])  # habit[1] = name

    return names


# Return the habits with periodicity (daily/weekly)
def get_habits_by_periodicity(periodicity):
    habits = database.get_all_habits()
    result = []

    for habit in habits:
        if habit[3] == periodicity:  # habit[3] = periodicity
            result.append(habit)

    return result
