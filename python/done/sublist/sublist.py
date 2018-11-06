SUBLIST = 0 
SUPERLIST = 1
UNEQUAL = 2
EQUAL = 3

def check_lists(first_list, second_list):

    x = set(first_list)  
    y = set(second_list)

    if x == y:
        if len(first_list) == len(second_list):
            newvalue = unequalsublist(first_list, second_list, 3) 
            return newvalue
        else:
            return 2
    elif x.issubset(y):
        newvalue = unequalsublist(first_list, second_list, 0) 
        return newvalue
    elif x.issuperset(y):
        newvalue = unequalsublist(second_list, first_list, 1)   
        return newvalue
    else:
        return 2


def unequalsublist(first_list, second_list, value):
    length = len(first_list)
    # get list of sublists
    lofl = [second_list[index:index+length] for index, a in enumerate(second_list)]
    empty_check = len(first_list) == 0 and len(second_list) == 0
    if not empty_check and first_list not in lofl:
        return 2
    else:
        return value

