from datetime import date

def meetup_day(year, month, day_of_the_week, which):
    teenth_array = [13,14,15,16,17,18,19]
    days_of_the_week = {0: "Sunday",
                             1: "Monday",
                             2: "Tuesday",
                             3: "Wednesday",
                             4: "Thursday",
                             5: "Friday",
                             6: "Saturday",
                            7: "Sunday"}

    target_day = day_of_the_week
    for x in teenth_array:
      date = date(year, month, x)
      if date.weekday()

    return date(2013, 5, 13)



meetup_day(2013, 5, 'Monday', 'teenth'), date(2013, 5, 13))



