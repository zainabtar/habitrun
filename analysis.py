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

from datetime import datetime


def get_longest_streak_for_habit(habit_id):
    completions = database.get_completions_for_habit(habit_id)

    if len(completions) == 0:
        return 0

    # Convert timestamps to date objects
    dates = []
    for ts in completions:
        date = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S").date()
        dates.append(date)

    # Sort dates
    dates.sort()

    longest_streak = 1
    current_streak = 1

    for i in range(1, len(dates)):
        difference = (dates[i] - dates[i - 1]).days

        if difference == 1:
            current_streak += 1
        else:
            current_streak = 1

        if current_streak > longest_streak:
            longest_streak = current_streak

    return longest_streak
