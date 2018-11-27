def handshake(code):
    keys = ['1', '10', '100', '1000']
    values = ['wink', 'double blink', 'close your eyes', 'jump']
    instructions = []
    resultscode = []
    # generate binary string
    binarystring = list("{0:b}".format(code))
    counter = 0
    while len(binarystring) > 0:
        x = binarystring.pop()
        if x == '1':
            instructions.append(x + '0' * counter)
        counter += 1
    inst = dict(zip(keys, values))
    for instruction in instructions:
        if instruction == '10000':
            continue
        else:
            resultscode.append(inst[instruction])
    if '10000' in instructions:
        resultscode = resultscode[::-1]
    return resultscode




def secret_code(actions):
    keys = [1, 10, 100, 1000]
    values = ['wink', 'double blink', 'close your eyes', 'jump']                                                                        
    resultscode = []
    reverse = False
    # TODO work out a way to determine if actions are reversed or not
    if len(actions) > 1:
        if 'jump' in actions:
            if actions.index('jump') == 0:
                reverse = True
        elif 'close your eyes' in actions and not 'jump' in actions:
            if actions.index('close your eyes') == 0:
                reverse = True
        elif 'wink' in actions and actions.index('wink') != 0:
                reverse = True

    inst = dict(zip(values, keys))
    if reverse:
        result = 10000
    else:
        result = 0 
    for action in actions:
        result += inst[action]
    return int(str(result), 2)
                

