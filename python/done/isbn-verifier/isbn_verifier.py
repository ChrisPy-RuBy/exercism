def verify(isbn):
  isbn_dedash = isbn.replace("-", "")

# this catch here is not very dry
# I don't really like having multiple returns in one function
  if len(isbn_dedash) != 10:
    return False



  validate_total = 0
  for index, value in enumerate(isbn_dedash):
    try: 
      if index == 9 and value == "X":
        validate_total += 10 
      else:
        validate_total += int(value) * (10 - index)
    except:
      valid = False

  valid = validate_total % 11 == 0
  
  return valid



print (verify('3-598-21508-8'))