from datetime import date

def generate_month(year, month):

  month_dict = dict()
  day = 1

  while True:
    try:
      week_day = date(year, month, day).weekday()
      month_dict[day] = week_day
      day += 1
    except ValueError:
      break
  return month_dict

def split_month(month_dict, which):

  split_month = {
    '1st': dict(),
    '2nd': dict(),
    'teenth': dict(),
    '3rd': dict(),
    '4th': dict(),
    '5th': dict(),
    'last': dict()
  }


  if which == "teenth":
    for date, day in month_dict.items():
      if date < 20 and date > 12:
        split_month['teenth'][date] = day  
      elif date <= 12 and date > 5:
        split_month['2nd'][date] = day
      elif date  <= 5:
        split_month['1st'][date] = day
      elif date >= 20 and date <= 26:
        split_month['3rd'][date] = day
      elif date > 26:
        split_month['4th'][date]  = day

  elif which == 'last':
    for date, day in month_dict.items():
      if date > (len(month_dict) - 7):
        split_month['last'][date] = day 


  else: 
    for date, day in month_dict.items():
      if date < 8:
        split_month['1st'][date] = day  
      elif date < 15:
        split_month['2nd'][date] = day
      elif date < 22:
        split_month['3rd'][date] = day
      elif date < 29:
        split_month['4th'][date] = day
      else:
        split_month['5th'][date]  = day
    

  # print (split_month)
  return split_month[which]




def meetup_day(year, month, day_of_the_week, which):

  days_of_the_week = { "Monday": 0,
                       "Tuesday": 1,
                       "Wednesday": 2,
                       "Thursday": 3,
                       "Friday": 4,
                       "Saturday": 5,
                       "Sunday": 6,
                      }

  month_dict = generate_month(year, month)
  meetup_dict = split_month(month_dict, which)

  for k, v in meetup_dict.items():
    if days_of_the_week[day_of_the_week] == v:
      meetup_date = k 

  return date(year, month, meetup_date)

print (meetup_day(2013, 8, 'Wednesday', '2nd'))
