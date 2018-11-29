def is_paired(input_string):

    openbracket = {}
    result = True

    for char in input_string: 
        if char in ['[', '(', '{']:
            openbracket[char] = True
        if char in [']', ')', '}'] and openbracket.get(char, None):
            openbracket[char] = False

    if True in openbracket.values():
      result = False
    return result




print(is_paired('[]'))
            

