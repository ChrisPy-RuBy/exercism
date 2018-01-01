def reverse(input=''):
  reversed_string = ""
  if input == '':
    return reversed_string
  else:
    y = (list(input)).__reversed__()
    for z in y:
      reversed_string += z
    return reversed_string


    
print (reverse('') == '')
print (reverse('robot') == 'tobor')
print (reverse('Ramen') == 'nemaR')
print (reverse('I\'m hungry!') == '!yrgnuh m\'I')
print (reverse('racecar') == 'racecar')