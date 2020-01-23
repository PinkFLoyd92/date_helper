from datetime import datetime, timedelta
import unittest, os, sys

sys.path.append(os.path.abspath('..'))

from calendario_bananero import CalendarioBananero


class TestDatehelper(unittest.TestCase):
    """
    Tested according to dates available in http://190.90.66.114:8080/banasan/index.php?module=calendar&view=0&PHPSESSID=&ano=2017&mes=0&cal=2
    """

    def __init__(self, *args, **kwargs):
        super(TestDatehelper, self).__init__(*args, **kwargs)
        self.gen_test_data()

    def gen_test_data(self):
        dates = {
            2021: datetime.now().date().replace(year=2021, month=1, day=1),
            2020: datetime.now().date().replace(year=2019, month=12, day=29),
            2019: datetime.now().date().replace(year=2018, month=12, day=30),
            2018: datetime.now().date().replace(year=2017, month=12, day=28)
        }

        self.date_helper = CalendarioBananero(dates)

    def test_get_leap(self):
        self.assertEqual(self.date_helper.get_leap(2019).days, 0, "Should be 0")

    def test_get_leap_2(self):
        self.assertEqual(self.date_helper.get_leap(2018).days, -3, "Should be -3")

    def test_get_weekdates_range(self):
        range = self.date_helper.get_weekdates_range(2019, 1)
        self.assertEqual(range[0], datetime.now().date().replace(year=2018, month=12, day=30), "Should be equal to 2018-12-30")

        self.assertEqual(range[1], datetime.now().date().replace(year=2019, month=1, day=5), "Should be equal to 2019-1-05")

    def test_get_weekdates_range2(self):
        range = self.date_helper.get_weekdates_range(2019, 40)
        self.assertEqual(range[0], datetime.now().date().replace(year=2019, month=9, day=29), "Should be equal to 2019-9-29")
        self.assertEqual(range[1], datetime.now().date().replace(year=2019, month=10, day=5), "Should be equal to 2019-10-5")

    def test_get_week_from_date(self):
        semana = self.date_helper.get_week_from_date(2019, datetime.now().date().replace(year=2018, month=12, day=30))
        self.assertEqual(semana, 1, "Should be equal to 1")

    def test_get_week_from_date2(self):
        semana = self.date_helper.get_week_from_date(2019, datetime.now().date().replace(year=2019, month=10, day=1))

        self.assertEqual(semana, 40, "Should be equal to 40")


    def test_get_week_from_date3(self):
        semana = self.date_helper.get_week_just_from_date(datetime.now().date().replace(year=2018, month=12, day=29))

        self.assertEqual(semana, 52, "Should be equal to 52")

    def test_get_week_from_date4(self):
        semana = self.date_helper.get_week_just_from_date(datetime.now().date().replace(year=2018, month=12, day=30))

        self.assertEqual(semana, 1, "Should be equal to 1")

    def test_get_week_from_date5(self):
        semana = self.date_helper.get_week_just_from_date(datetime.now().date().replace(year=2019, month=12, day=31))

        self.assertEqual(semana, 1, "Should be equal to 1")

    def test_get_week_from_date6(self):
        semana = self.date_helper.get_week_just_from_date(datetime.now().date().replace(year=2020, month=1, day=3))

        self.assertEqual(semana, 1, "Should be equal to 1")


    def test_get_periodos_from_range(self):
        # 2019
        range = self.date_helper.get_periods_date_range(2019, 1)
        self.assertEqual(range[0], datetime.now().date().replace(year=2018, month=12, day=30), "Should be equal to 2018-12-30")
        self.assertEqual(range[1], datetime.now().date().replace(year=2019, month=1, day=19), "Should be equal to 2019-10-5")

    def test_get_last_day(self):
        self.assertEqual(self.date_helper.get_last_date(2019), datetime.now().date().replace(year=2019, month=12, day=28), "Should be equal to 2019-12-28")

    def test_period_dates_2020(self):
        # 2020
        range = self.date_helper.get_periods_date_range(2020, 1)
        self.assertEqual(range[0], datetime.now().date().replace(year=2019, month=12, day=29), "Should be equal to 2019-12-29")
        self.assertEqual(range[1], datetime.now().date().replace(year=2020, month=1, day=18), "Should be equal to 2020-1-21")

    def test_period_dates_2018(self):
        # 2020
        range = self.date_helper.get_periods_date_range(2018, 1)
        self.assertEqual(range[0], datetime.now().date().replace(year=2017, month=12, day=28), "Should be equal to 2017-12-28")
        self.assertEqual(range[1], datetime.now().date().replace(year=2018, month=1, day=17), "Should be equal to 2018-1-17")

    def test_get_all_dates_2018(self):
        # 2020
        range = self.date_helper.get_date_range_from_year(2018)
        self.assertEqual(range[0], datetime.now().date().replace(year=2017, month=12, day=28), "Should be equal to 2017-12-28")
        self.assertEqual(range[1], datetime.now().date().replace(year=2018, month=12, day=29), "Should be equal to 2018-12-29")

    def test_get_weeks_from_year(self):
        range_2018 = self.date_helper.get_weeks(2018)
        range_2019 = self.date_helper.get_weeks(2019)

        self.assertEqual(range_2018, 52, "Should be equal to 52")
        self.assertEqual(range_2019, 52, "Should be equal to 52")


if __name__ == '__main__':
    unittest.main()
