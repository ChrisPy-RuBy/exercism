import re

def is_isogram(string):
    string = string.lower().split(" ")
    num_strip = re.sub(r'\d\W', "", string)
    print num_strip
    return len(set(string)) == len(list(string))



print is_isogram("test")
print is_isogram("Aleph Bot Chap")
print is_isogram("accentor")
print is_isogram("isogram")