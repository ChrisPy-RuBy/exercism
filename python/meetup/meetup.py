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



def meetup_day(year, month, day_of_the_week, which):

    days_of_the_week = { 0: "Monday",
                         1: "Tuesday",
                         2: "Wednesday",
                         3: "Thursday",
                         4: "Friday",
                         5:"Saturday",
                         6: "Sunday",
                        }

    first_day = (date(year, month, 1)).weekday()
    print (first_day)
    print (days_of_the_week[first_day])                         

    for x in month_dict[which]:
        day = date(year, month, x)
        if days_of_the_week[day.weekday()] == day_of_the_week:
            return (date(year, month, x))
        # else:
        #     continue



# meetup_day(2013, 5, 'Monday', 'teenth')
generate_month(2013, 5)

                        