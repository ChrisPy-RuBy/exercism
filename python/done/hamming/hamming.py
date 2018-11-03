import pprint


def distance(string1, string2):
  list1 = list(string1)
  list2 = list(string2)
  stitched_dict = {}
  counter = 0
  distance = 0
  for x in list1:
    if len(list1)  == len(list2):
      stitched_dict[x + str(counter)] = list2[counter] + str(counter)
      counter += 1
    else: 
      raise ValueError("incorrect input length")
  for x in stitched_dict:
    if stitched_dict[x] != x:
      distance += 1 
  return distance
  

