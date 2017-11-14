from datetime import date

def meetup_day(year, month, day_of_the_week, which):
    month_dict = {  '1st': [1,2,3,4,5,6,7],
                    '2nd': [8,9,10,11,12,13,14],
                    'teenth': [13,14,15,16,17,18,19],
                    '3rd': [20,21,22,23,24,25,26],
                    '4th': [27,28,29,30]
                    }



    days_of_the_week = { 0: "Monday",
                         1: "Tuesday",
                         2: "Wednesday",
                         3: "Thursday",
                         4: "Friday",
                         5:"Saturday",
                         6: "Sunday",
                        }
                         

    for x in month_dict[which]:
        day = date(year, month, x)
        if days_of_the_week[day.weekday()] == day_of_the_week:
            return (date(year, month, x))
        # else:
        #     continue



meetup_day(2013, 5, 'Monday', 'teenth')


# days_of_the_week = { 0: "Sunday",
#                      1: "Monday",
#                      2: "Tuesday",
#                      3: "Wednesday",
#                      4: "Thursday",
#                      5: "Friday",
#                      6:"Saturday",
#                      7: "Sunday",
#                     }
                        