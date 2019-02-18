class Cipher(object):
"""
sdfsaf:w
:q
dfgsdfgsdfgsdfgdg:wdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd"""


    def __init__(self, key=None):
        self.key = key

    def encode(self, text):
        self.key = text[:len(text)]
        return text

    def decode(self, text):
        self.key = text[:len(text)]
        return text
