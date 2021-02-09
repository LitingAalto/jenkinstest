import unittest
from datetime import date
from weekday.weekdays import weekdays


class TestWeekdays(unittest.TestCase):
    """Implement tests for weekdays here."""
    def test_calculation(self):
        self.assertEqual(weekdays(date(2020, 8, 17), date(2020, 8, 20)), 32)

    def test_weekdends(self):
        self.assertEqual(weekdays(date(2020, 8, 16), date(2020, 8, 22)), 40)


if __name__ == "__main__":
    unittest.main()