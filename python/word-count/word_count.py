import re

def word_count(sentence):
  stripped_string  = re.sub(r'[^a-zA-Z\s0-9]', " ", sentence)
  rem_whtspace = stripped_string.lower().split()
  checker_list = set(rem_whtspace)
  final_dict = {} 
  print (checker_list)
  for x in checker_list:
    final_dict[x] = rem_whtspace.count(x)
  return final_dict 





