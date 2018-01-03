from string import ascii_lowercase
import string

def encode(plain_text):

  plain_text = plain_text.lower().strip().replace(" ", "")
  exclude = string.punctuation
  plain_text = ''.join(ch for ch in plain_text if ch not in exclude)

  encoded = ""
  cypher = dict(zip(ascii_lowercase, ascii_lowercase[::-1]))
  for i, x in enumerate(plain_text):
    try:
      if (i != 0) and (i % 5 == 0):
        encoded += (' ' + cypher[x]) 
      else:
        encoded += cypher[x]
    except KeyError:
        encoded += x
  return encoded


def decode(ciphered_text):
    pass
