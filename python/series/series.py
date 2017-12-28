def slices(series, length):
    results = []
    series = [int(x) for x in list(series)]

    # if len(series) < length or length != 0:
    #   print (length, len(series)) 
    # else:
    #    raise ValueError("nob jockey")
    try:
      if len(series) >= length and length != 0:
        for index, x in enumerate(series):
          y = series[index:(index+length)]
          if len(y) == length:
            results.append(y)
          else:
            continue
        return results
      else: 
          raise ValueError("Wrong numbers")
    except ValueError:
       raise   


# print (slices("012", 4))
# print (slices("01234", 0))
