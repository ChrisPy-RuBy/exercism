
# number_map = {
#   '1': "one",
#   '2': "two",
#   '3': "three",
#   '4': "four",
#   '5': "five",
#   '6': "six",
#   '7': "seven",
#   '8': "eight",
#   '1,': "one,",
#   '2,': "two,",
#   '3,': "three,",
#   '4,': "four,",
#   '5,': "five,",
#   '6,': "six,",
#   '7,': "seven,",
#   '8,': "eight,",
#   '9,': "nine,",
# }


def hey(phrase):
    phrase = phrase.strip()
    if phrase.isupper():
        return 'Whoa, chill out!'
    elif phrase[-1:] == '?':
        return 'Sure.'
    elif phrase == '':
        return 'Fine. Be that way!'
    else:
        return 'Whatever.'




# def number_replacer(listy):
  # this is a method to replace all the numbers with their corresponding words. I didn't use it as it become too difficult dealing with punctuation. But it would be good to go back and figure out how to implement it.

#   numbers_to_words = []
#   remake_phrase =""
#   for word in listy:
#     if word in number_map:
#       numbers_to_words.append(number_map[word])
#     else:
#       numbers_to_words.append(word)
#   for x in numbers_to_words:
#     remake_phrase += (x + " ")
#   phrase = remake_phrase.strip()
#   return phrase
    

# hey("1, 2, 3 GO!")
# hey("1, 2, 3")
# hey("4?")