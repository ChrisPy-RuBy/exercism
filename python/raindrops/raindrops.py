def raindrops(number):
    resultstring = str(number)

    def ing_ang_ong(number, tocheck):
        lookup = {
                  3: 'Pling',
                  5: 'Plang',
                  7: 'Plong',
                 }
        if number % tocheck == 0:
            return lookup[tocheck]
        return ""

    x = [ing_ang_ong(number, 3),
         ing_ang_ong(number, 5),
         ing_ang_ong(number, 7)]

    if any(x):
        resultstring = "".join(x)
    return resultstring
