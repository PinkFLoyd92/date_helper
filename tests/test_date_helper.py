from datetime import datetime, timedelta
import unittest, os, sys
sys.path.append(os.path.abspath('..'))

from date_helper_pkg import DateHelper


class TestDatehelper(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestDatehelper, self).__init__(*args, **kwargs)
        self.gen_test_data()

    def gen_test_data(self):
        dates = {
            2019: datetime.now().date().replace(year=2019, month=1, day=4),
            2018: datetime.now().date().replace(year=2017, month=12, day=28)
        }

        self.date_helper = DateHelper(dates)

    def test_get_leap(self):
        self.assertEqual(self.date_helper.get_leap(2019).days, 3, "Should be 3")

    def test_get_leap_2(self):
        self.assertEqual(self.date_helper.get_leap(2018).days, -4, "Should be -4")


    def test_get_weekdates_range(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_week_from_date(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def get_periods_date_range(self):
        pass


if __name__ == '__main__':
    unittest.main()
