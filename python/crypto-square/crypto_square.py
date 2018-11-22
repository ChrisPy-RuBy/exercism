import re
from collections import OrderedDict

def encode(plain_text):
    # string formatting
    # lowercase and strip leadingtrailedwhitespace
    plain_text = plain_text.lower()
    # strip non-alphanumeric characters 
    pattern = re.compile('[\W_]+')
    plain_text = pattern.sub('', plain_text)
    textlength = len(plain_text)
    print('plain text', plain_text)
    # work out c and r
    c = 0
    r = 0
    while c**2 < textlength:
        c += 1    
    if c**2 == textlength:
        r = c
    else: 
        r = c-1
    print(c, r, c*r, textlength)  

    if r == 0:
        return plain_text
    else:
        # split string into correct length
        outputstring = ''    
        derp = [plain_text[i:i+c] for i in range(0, textlength, c)]
        print('derp', derp)
        # Format list
        outputstring =  ''
        indexdict = OrderedDict()
        for index in range(0, r+1):
            indexdict[index] = ''
            for subword in derp:
                try:
                    indexdict[index] += subword[index]
                except IndexError:
                    indexdict[index] += ' '
        print('indexdict', indexdict)
        for k, v in indexdict.items():
            print(k, v, r-1)
            if k == r:
                print('here')
                outputstring += v
            else:
                outputstring += v + ' '
    return outputstring
    

print(encode('chill out'))
print(encode('Chill Out.'))
print(encode('This is fun!'))
