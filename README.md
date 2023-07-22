[![Build Status](https://github.com/pinkfloydsito/calendario-bananero/actions/workflows/test.yml/badge.svg)](https://github.com/pinkfloydsito/calendario-bananero/actions/workflows/test.yml)

**CalendarioBananero - Banana Calendar**

**Description**
CalendarioBananero is a Python class that provides functionality to work with a custom calendar system, referred to as the "Banana Calendar." This calendar system has some unique features, such as starting dates for each year being predefined and variable week lengths due to leap weeks. The class allows users to perform various operations related to weeks, periods, and date ranges within this Banana Calendar.

**Installation**
The CalendarioBananero class requires the epiweeks, coveralls libraries, which can be installed using pipenv:

```
pipenv install
```

**Usage**

1. **Initialization**

   To use the CalendarioBananero class, you need to create an instance of the class by passing a dictionary containing the initial dates of each year in the Banana Calendar as an argument.

   ```python
   from datetime import datetime
   from epiweeks import Week, Year
   from CalendarioBananero import CalendarioBananero

   # Dictionary containing initial dates of each year
   dates = {
       2021: datetime(2021, 1, 4),  # January 4, 2021
       2022: datetime(2022, 1, 3),  # January 3, 2022
       # Add more years and corresponding dates as needed
   }

   # Create an instance of CalendarioBananero
   banana_calendar = CalendarioBananero(dates)
   ```

2. **Get Total Weeks in a Year**

   You can get the total number of weeks in a given year in the Banana Calendar.

   ```python
   year = 2022
   total_weeks = banana_calendar.get_weeks(year)
   print(f"Total weeks in {year}: {total_weeks}")
   ```

3. **Get Leap Days in a Year**

   You can find out the number of leap days (extra days) present in a specific year due to leap weeks.

   ```python
   year = 2022
   leap_days = banana_calendar.get_leap(year)
   print(f"Leap days in {year}: {leap_days.days}")
   ```

4. **Get the Date Range of a Week**

   You can get the start and end dates of a week in a given year and week number.

   ```python
   year = 2022
   week = 4
   start_date, end_date = banana_calendar.get_weekdates_range(year, week)
   print(f"Week {week} in {year} starts on {start_date} and ends on {end_date}")
   ```

5. **Get the Week Number from a Date**

   You can determine the week number of a specific date in the Banana Calendar.

   ```python
   year = 2022
   date = datetime(2022, 1, 22)  # January 22, 2022
   week_number = banana_calendar.get_week_from_date(year, date)
   print(f"Week number of {date} in {year}: {week_number}")
   ```

6. **Get the Week Number Just from a Date**

   This method determines the week number of a date, considering it may fall into the previous or next year if it's close to the boundary.

   ```python
   date = datetime(2021, 12, 31)  # December 31, 2021
   week_number = banana_calendar.get_week_just_from_date(date)
   print(f"Week number just from {date}: {week_number}")
   ```

7. **Get the Period Number from a Date**

   In the Banana Calendar, weeks are grouped into periods (sets of three weeks). You can find out the period number to which a specific date belongs.

   ```python
   year = 2022
   date = datetime(2022, 2, 15)  # February 15, 2022
   period_number = banana_calendar.get_period_from_date(year, date)
   print(f"Date {date} in {year} belongs to period {period_number}")
   ```

8. **Get the Date Range of a Period**

   You can obtain the start and end dates of a specific period in a given year.

   ```python
   year = 2022
   period = 2
   start_date, end_date = banana_calendar.get_periods_date_range(year, period)
   print(f"Period {period} in {year} starts on {start_date} and ends on {end_date}")
   ```

9. **Get the Last Date of a Year**

   This method returns the last date of a specific year in the Banana Calendar.

   ```python
   year = 2022
   last_date = banana_calendar.get_last_date(year)
   print(f"Last date of {year}: {last_date}")
   ```

10. **Get the Date Range of a Year**

    You can retrieve the start and end dates of a specific year in the Banana Calendar.

    ```python
    year = 2022
    start_date, end_date = banana_calendar.get_date_range_from_year(year)
    print(f"Year {year} starts on {start_date} and ends on {end_date}")
    ```

**Note:**
- The Banana Calendar uses leap weeks, which can introduce variations in week lengths and make week-based calculations more complex.
- Make sure to provide correct initial dates for each year when initializing the CalendarioBananero class, as this is crucial for accurate date calculations.
