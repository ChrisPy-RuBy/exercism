from string import ascii_lowercase
import string

cypher = dict(zip(ascii_lowercase, ascii_lowercase[::-1]))

def encode(plain_text):

  plain_text = plain_text.lower().strip().replace(" ", "")
  exclude = string.punctuation
  plain_text = ''.join(ch for ch in plain_text if ch not in exclude)

  encoded = ""
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

    decypher = dict((k,v) for k,v in cypher.items())
    decoded = ""
    ciphered_text = ciphered_text.replace(" ","")


    for i, x in enumerate(ciphered_text):
      try:
          decoded += decypher[x]
      except KeyError:
          decoded += x
    return decoded

    
