
def decode(string):
  return ''


def encode(encoding):

  previous_letter = ""
  counter = 0
  tally = 0
  encoded = ""
  for x in encoding:
    counter += 1
    print(x , counter)
    # this part is to deal with last part of the sequence
    if counter == len(encoding):
      if tally == 1:
        encoded += x
      else:
        print("here", (tally), previous_letter, x)
        encoded += (str(tally) + previous_letter + x)
    # this increases the tally is a letter is duplicated
    elif x == previous_letter:
      tally += 1
      previous_letter = x

    # this deals with the letter changing and reseting the tally
    else:
      # this checks whether it is first letter or not
      if previous_letter != "":
        print("here", x)
        if tally == 1:
          encoded += previous_letter
           # encoded += x
        else: 
          encoded += (str(tally) + previous_letter)
    #  this problem is her
      tally = 1
      previous_letter = x
  return encoded


print (encode('AABBBCCCC'))
print (encode('XYZ'))
print (encode('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB'),
'12WB12W3B24WB')
# print (encode(''))
# 12WB12W3B24W23W 
# 12WB12W3B24WB
12WB12W3B24WB 
12WB12W3B24WB

