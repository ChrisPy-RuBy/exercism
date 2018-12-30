def is_paired(input_string):
    
    lookup = {"{": "}", 
              "[": "]",
              "(": ")"}
    result = True

    for index, letter in enumerate(input_string):
        print(letter)
        if letter in lookup.keys():
            for index, newletter in enumerate(input_string[index:]):
                print('1', index, newletter, input_string[index:])
                if newletter == lookup[letter]:
                    input_string.pop(index)

                elif newletter in lookup.values() and newletter != lookupletter:
                    result = False
                elif newletter not in lookup.values():
                    result = False



    
    return result


print(is_paired('{}'))
print(is_paired('}{'))

print(is_paired('([{])'))
            

