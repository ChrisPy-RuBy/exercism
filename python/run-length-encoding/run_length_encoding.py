import pprint as pprint 

def decode(string):

  # parse string 

  previousnumber = 0
  number_string = "" 
  output_string = ""
  for x in string: 
    try:
      int(x)
      if previousnumber != 0:  
        number_string += str(previousnumber)
        previousnumber = int(x)
      else:
        previousnumber = int(x)
    except:
        number_string += str(previousnumber)
        if previousnumber != 0:
          output_string += ("," + number_string + "," + x )
        else: 
          output_string += ("," + x )
        number_string = ""
        previousnumber = 0
    
  parsed_list = output_string.split(",")
  parsed_list.pop(0)
  
  counter = 1
  output_string = ""

  for x in parsed_list:
    try:
      if int(x):
        counter = int(x)
    except:
      if counter == 1:
        output_string += x
      else:
        expanded_string = (counter * x) 
        output_string += expanded_string
      counter = 1
  print (output_string)
        

decode("12A3C")

decode("12AB3C")

def encode(encoding):

  previous_letter = ""
  counter = 0
  tally = 0
  encoded = ""
  for x in encoding:
    counter += 1
    # print(x , counter)
    # this part is to deal with last part of the sequence
    if counter == len(encoding):
      if x == previous_letter:
         encoded += (str(tally + 1) + x)
      elif tally == 1:
        encoded += previous_letter + x
      else:
        # print("here", (tally), previous_letter, x)
        encoded += (str(tally) + previous_letter + x)
    # this increases the tally is a letter is duplicated

    elif x == previous_letter:
      tally += 1
      previous_letter = x

    # this deals with the letter changing and reseting the tally
    else:
      # this checks whether it is first letter or not
      if previous_letter != "":
        # print("here", x)
        if tally == 1:
          encoded += previous_letter
           # encoded += x
        else: 
          encoded += (str(tally) + previous_letter)
    #  this problem is her
      tally = 1
      previous_letter = x
  return encoded


