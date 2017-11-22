from datetime import date
import pprint

def generate_month(year, month):

    month_dict = {  '1st': {},
                    '2nd': {},
                    'teenth': {},
                    '3rd': {},
                    '4th': {}
                }
    week_dict = dict()
    day_counter = 1

    for x in month_dict:
        while day_counter % 7 != 0 :
            try:
                week_dict[day_counter] = date(year, month,day_counter).weekday()
                day_counter += 1
            except ValueError:
                month_dict[x] = week_dict 
                break
        else:
            week_dict[day_counter] = date(year, month,day_counter).weekday()
            month_dict[x] = week_dict
            continue
        day_counter += 1
    return month_dict

print (generate_month(2016, 2))

def meetup_day(year, month, day_of_the_week, which):

    month_dict = generate_month(year, month)

    days_of_the_week = { "Monday": 0,
                         "Tuesday": 1,
                         "Wednesday": 2,
                         "Thursday": 3,
                         "Friday": 4,
                         "Saturday": 5,
                         "Sunday": 6,
                        }
                       

    print (month_dict[which])




                        