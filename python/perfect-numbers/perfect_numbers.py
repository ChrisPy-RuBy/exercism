def classify(number):

    # data sniff
    # number greater than 0
    if number <= 0:
        raise ValueError('Need numbers bigger than 0') 

    factors = [x for x in range(1, number-1) if number % x == 0]
    sum_ = sum(factors)

    if sum_ == number:
        result = 'perfect'
    elif sum_ < number:
        result = 'deficient'
    elif sum_ > number:
        result = 'abundant'
    else:
        raise "shouldn't get here"
    return result

print(classify(28))
print(classify(1))



