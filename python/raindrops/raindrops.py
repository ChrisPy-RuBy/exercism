def raindrops(number):

    lookup = {
              3: 'Pling',
              5: 'Plang',
              7: 'Plong',
             }
    res = "".join([v for k, v in sorted(lookup.items()) if number % k == 0])

    # I didn't know you could do this!
    return res or str(number)
