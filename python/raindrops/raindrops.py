def raindrops(number):
    resultstring = str(number)

    def ing_ang_ong(tocheck):
        lookup = {
                  3: 'Pling',
                  5: 'Plang',
                  7: 'Plong',
                 }
        if number % tocheck == 0:
            return lookup[tocheck]
        return ""

    results = [ing_ang_ong(3),
               ing_ang_ong(5),
               ing_ang_ong(7)]

    if any(results):
        resultstring = "".join(results)
    return resultstring
