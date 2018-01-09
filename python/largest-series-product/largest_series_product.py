def largest_product(series, size):

  

    largest_product = 0  
    for index, value in enumerate(series):
      x =  series[index : index + size]
      running_total = 1
      for y in x:
        running_total *= int(y)
      if running_total > largest_product:
        largest_product = running_total
  
    return largest_product
