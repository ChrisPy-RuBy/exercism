def abbreviate(words):

  results = ""

  for x in words.lower().title():
    if x.isupper():
      results += x
  return results

