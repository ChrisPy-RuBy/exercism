from collections import Counter

def detect_anagrams(word, candidates):

  # Case matching here is quite hacky. Come up with a better way to do this!

  letter_counter = Counter(word.lower())

  counter_list = []

  for x in candidates:

    z = x.lower()
    y = Counter(z)
    if y == letter_counter:
      if z not in counter_list and z != word.lower():
        counter_list.append(x)

  return (counter_list)