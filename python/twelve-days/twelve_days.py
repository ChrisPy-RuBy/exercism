def recite(start_verse, end_verse):

    has_and = "and " if end_verse > 1 else ""
    lexical_dict = {
            12: ("twelfth", "twelve Drummers Drumming, "),
            11: ("eleventh", "eleven Pipers Piping, "),
            10: ("tenth", "ten Lords-a-Leaping, "),
            9:  ("ninth", "nine Ladies Dancing, "),
            8:  ("eighth", "eight Maids-a-Milking, "),
            7:  ("seventh", "seven Swans-a-Swimming, "),
            6:  ("sixth", "six Geese-a-Laying, "),
            5:  ("fifth", "five Gold Rings, "),
            4:  ("fourth", "four Calling Birds, "),
            3:  ("third", "three French Hens, "),
            2:  ("second", "two Turtle Doves, "),
            1:  ("first", "{}a Partridge in a Pear Tree.".format),
            0:  "On the {} day of Christmas my true love gave to me: ".format
            }
    verses = []
    verse_num = start_verse
    for verse in range(start_verse, end_verse+1):
        has_and = "and " if verse_num > 1 else ""
        last_line = [lexical_dict[1][1](has_and)]
        first_line = [lexical_dict[0](lexical_dict[verse_num][0])]
        verse_lines = [lexical_dict[line][1] for line in range(verse_num, 1, -1)]
        verse = "".join(first_line + verse_lines + last_line)
        verses.append(verse)
        verse_num += 1
    return verses
