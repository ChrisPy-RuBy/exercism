def is_armstrong(number):
    arr = list(str(number))
    sum = 0
    for x in arr:
      sum += (int(x)** len(arr))
    if number == sum:
      return True
    else:
      return False


    
