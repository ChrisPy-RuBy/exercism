def sieve(limit):
    starting_values = [x for x in range(1, limit+1, 2) if x != 1]
    results = []
    if limit <= 1:
      return results
    else:
      results.append(2)
      derp = checkprime(starting_values)
      [results.append(x) for x in derp]
    return results 

def checkprime(starting_point):
  for x in starting_point:
    for y in starting_point:
      if (y % x == 0) and (x != y):
        starting_point.pop(starting_point.index(y))
      else:
        continue  
  return starting_point
