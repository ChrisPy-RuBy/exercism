
def decode(string):
  return ''


def encode(encoding):

  previous_letter = ""
  counter = 0
  tally = 0
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



print (encode('XYZ'))
print (encode(''))

