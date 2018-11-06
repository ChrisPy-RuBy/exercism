import logging
import math

def triplets_with_sum(sum_of_triplet):

    # sum = a + b + sqrt(a^2 + b^2)

    maxrange1 = sum_of_triplet / 2 
    maxrange2 = int(maxrange1 / 1.25)
    triplets = set() 
    #brute force
    x = ([a, b] for a in range(1, maxrange1) for b in range(1, maxrange2) if a != b) 
    for number in x:
        number.sort()
        assert(len(number) == 2)
        c = math.sqrt(number[0]**2 + number[1]**2)
        if (sum(number) + c) == sum_of_triplet:
            # is_triplet will change state so use a copy
            number.append(int(c))
            newnumber = list(number)
            if number[0] % 100 == 0:
                print(number)
            if is_triplet(newnumber):
                x = tuple(number) 
                triplets.add(x)
    return triplets
                        


def is_triplet(triplet):
    assert(type(triplet) == list)
    assert(min(triplet) >= 0)
    # pops the max value out of the triplet
    c = triplet.pop(triplet.index(max(triplet)))
    a,b = triplet
    if c ** 2 == a**2 + b** 2:
        return True
    else:
        return False


