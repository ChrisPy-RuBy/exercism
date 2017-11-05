# def encoding(string):
#   encoded_list = []
#   it = iter(string)
#   counter = 0


encoded_list = []


def encoder(encoding):
#   encoded_list = []
#   counter = 0
#   for x in encoding:
#     # print("x", x)
#     for y in encoding:
#       # print("y", y)
#       if x == y:
#         counter += 1
#         # print (counter, y)
#       else:
#         print (counter, x)
      
#     counter = 0 
#   print (encoded_list)

  # counter = 0

  # wanking = []
  # while counter < len(encoding):
  #   print(counter, encoding[counter])
  #   tally = 0 
  #   for x in encoding:
  #     if x == encoding[counter]:
  #       tally += 1
  #       print ('yes', tally)
  #     else:
  #       wanking.append(tally)
  #       print ('no', tally) 
  #   counter += 1
  # print (wanking) 

  previous_letter = ""
  counter = 0
  tally = 0
  listy = []
  encoded = ""
  for x in encoding:
    counter += 1
    if counter == len(encoding):
      encoded += (str(tally + 1) + x)
    elif x == previous_letter:
      tally += 1
    else:
      if previous_letter != "":
        encoded += (str(tally) + previous_letter)
      tally = 1
    previous_letter = x
  return encoded

print (encoder("AAABBB"))
