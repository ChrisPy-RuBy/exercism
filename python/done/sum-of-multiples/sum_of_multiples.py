def sum_of_multiples(limit, multiples): 
   
    if len(multiples) == 0 or limit < multiples[0]:
      return 0
    else:
      results = []
      for y in multiples:  
        for x in range(1, limit):
          if x % y == 0:
            results.append(x)

    return sum(set(results))

