def square_of_sum(num): 

  sum = 0 
  while num > 0:
    sum += num
    num -= 1
  return sum ** 2 


def sum_of_squares(num):
  sum = 0 
  while num > 0:
    sum += (num ** 2)
    num -= 1
  return sum 


def difference(num):

  return (square_of_sum(num) - sum_of_squares(num))
    
