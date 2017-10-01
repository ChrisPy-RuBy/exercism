import re


def is_pangram(string):
  processed_string = string.lower().replace(" ","")
  trimmed_string = re.findall(r'[a-zA-Z]', string)
  print trimmed_string
  if len(set(trimmed_string)) == 26:
    return True
  else:
    print len(set(trimmed_string))
    return False
