SUBLIST = 0 
SUPERLIST = 1
UNEQUAL = 2
EQUAL = 3

def check_lists(first_list, second_list):

    x = set(first_list)  
    y = set(second_list)
    if x == y:
        if len(first_list) == len(second_list):
            return 3
        else:
            return 2
    elif x.issubset(y):
            if     
        return 0
    elif x.issuperset(y):
        return 1
    else:
        return 2



