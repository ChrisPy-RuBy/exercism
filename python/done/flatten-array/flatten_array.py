def flatten(iterable):
  flattened_list = []

  def internal_function(iterable):  
    for item in iterable:
      if type(item) == list:
          internal_function(item)
      elif type(item) == int or type(item) == str:
        flattened_list.append(item)
      else:
        continue

  internal_function(iterable)

  return flattened_list