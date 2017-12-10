from collections import Counter

def detect_anagrams(word, candidates):

  letter_counter = Counter(word)
  counter_list = []

  for x in candidates:
    y = Counter(x)
    if y == letter_counter:
      print (y, letter_counter)
      counter_list.append(x)

  return (counter_list)
    
#   for index, candidate in enumerate(candidates):
#     for letter in candidate:
#       if letter in word:
#         continue
#       else:
#         candidates.pop(index)
#         break

#   return (candidates)


candidates = ["tan", "stand", "at"]
print (detect_anagrams("ant", candidates))
candidates = ["hello", "world", "zombies", "pants"]
print (detect_anagrams("diaper", candidates))