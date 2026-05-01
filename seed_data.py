# seed_data.py
# This file creates 4 weeks of example completion data
# for the predefined habits in the database.

from datetime import datetime, timedelta
import database


def add_example_tracking_data():
    """Add 4 weeks of example completion data for predefined habits."""

    habits = database.get_all_habits()

    # Stop if no habits exist yet
    if len(habits) == 0:
        return

    # Prevent duplicate example data
    existing = database.get_completions_for_habit(1)
    if len(existing) > 0:
        return

    # Start 28 days ago
    start_date = datetime.now() - timedelta(days=28)

    # Habit IDs based on predefined habits:
    # 1 = Drink Water (daily)
    # 2 = Exercise (daily)
    # 3 = Read (daily)
    # 4 = Call Family (weekly)
    # 5 = Clean Room (weekly)

    # Daily habit 1: completed every day for 7 days in a row,
    # then misses some days, then continues again
    for day in [0, 1, 2, 3, 4, 5, 6, 9, 10, 11, 15, 16, 17, 18]:
        completed_at = (start_date + timedelta(days=day)).strftime("%Y-%m-%d %H:%M:%S")
        database.add_completion_with_date(1, completed_at)

    # Daily habit 2: shorter streaks with more gaps
    for day in [0, 1, 4, 5, 8, 9, 12, 13, 20, 21]:
        completed_at = (start_date + timedelta(days=day)).strftime("%Y-%m-%d %H:%M:%S")
        database.add_completion_with_date(2, completed_at)

    # Daily habit 3: almost every other day
    for day in [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26]:
        completed_at = (start_date + timedelta(days=day)).strftime("%Y-%m-%d %H:%M:%S")
        database.add_completion_with_date(3, completed_at)

    # Weekly habit 4: completed once every week for 4 weeks
    for day in [0, 7, 14, 21]:
        completed_at = (start_date + timedelta(days=day)).strftime("%Y-%m-%d %H:%M:%S")
        database.add_completion_with_date(4, completed_at)

    # Weekly habit 5: completed only in 3 of the 4 weeks
    for day in [0, 7, 21]:
        completed_at = (start_date + timedelta(days=day)).strftime("%Y-%m-%d %H:%M:%S")
        database.add_completion_with_date(5, completed_at)