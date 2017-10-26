import datetime as datetime



def add_gigasecond(birth):
  giga = datetime.timedelta(0, 1000000000)
  aged = birth + giga
  return aged

