def largest_product(series, size):

  # counter for the largest product
  largest_product_col = 0

  # a bunch of catches for weird values etc
  if len(series) < size:
    raise ValueError("size is larger the series length")

  if len(series) == 0 or size == 0:
    largest_product_col = 1

  if size < 0:
    raise ValueError("this is negative")

    
  for index, value in enumerate(series):
    x = series[index: index + size]
    
    if ("0" in x) or len(x) != size :
      continue

    running_total = 1
    for y in x:
      try:
        running_total *= int(y)
      except ValueError:
        raise
    if running_total > largest_product_col:
      largest_product_col = running_total

  return largest_product_col



