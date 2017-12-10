import string

def rotate(text, key):

  alpha = list(string.ascii_lowercase)
  beta = list(alpha)

    
  counter = 0 
  while counter < key:
    generate_cypher(alpha)
    counter += 1

  translation_dict = dict()
  for index, letter in enumerate(beta):
    translation_dict[letter] = alpha[index]

  return encode(text, translation_dict)


def generate_cypher(alpha):
  alpha.append(alpha.pop(0))


def encode(text, cypher):
  encoded_string = ""
  for x in text:
      if x.isupper():
        x = x.lower()
        encoded_string += (cypher.get(x, x).upper())
      else:
        encoded_string += cypher.get(x, x)
  return encoded_string


