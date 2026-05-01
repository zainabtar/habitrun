# test_habits.py
# Basic unit tests for HabitRun

import unittest
import database
import analysis


class TestHabitRun(unittest.TestCase):

    def setUp(self):
        # Make sure database exists
        database.initialize_database()

    def test_get_all_habits(self):
        habits = database.get_all_habits()
        self.assertTrue(len(habits) >= 1)

    def test_get_habit_names(self):
        names = analysis.get_all_habit_names()
        self.assertTrue(len(names) >= 1)

    def test_filter_daily_habits(self):
        daily = analysis.get_habits_by_periodicity("daily")
        self.assertTrue(len(daily) >= 1)

    def test_streak_calculation(self):
        # test first habit (ID = 1)
        streak = analysis.get_longest_streak_for_habit(1)
        self.assertTrue(streak >= 1)


if __name__ == "__main__":
    unittest.main()
