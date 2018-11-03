import inflect
import string

def say(number):

  # it is cheating to use this inflect module I think

  try:
    if number >= 0 and number < 1e12:
      p = inflect.engine()
      word = p.number_to_words(int(number))
      return word.replace(',','')
    else:
      raise ValueError("please try a number between derp and derple")
  except ValueError:
    raise
  
