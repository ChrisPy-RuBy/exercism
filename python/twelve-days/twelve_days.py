
LEXICAL_LIST = [
            (None, "On the {} day of Christmas my true love gave to me: ".format),
            ("first", "{}a Partridge in a Pear Tree.".format),
            ("second", "two Turtle Doves"),
            ("third", "three French Hens"),
            ("fourth", "four Calling Birds"),
            ("fifth", "five Gold Rings"),
            ("sixth", "six Geese-a-Laying"),
            ("seventh", "seven Swans-a-Swimming"),
            ("eighth", "eight Maids-a-Milking"),
            ("ninth", "nine Ladies Dancing"),
            ("tenth", "ten Lords-a-Leaping"),
            ("eleventh", "eleven Pipers Piping"),
            ("twelfth", "twelve Drummers Drumming"),
            ]

def recite(start_verse, end_verse):

    has_and = "and " if end_verse > 1 else ""
    verses = []
    verse_num = start_verse
    for verse in range(start_verse, end_verse+1):
        has_and = "and " if verse_num > 1 else ""
        last_line = [LEXICAL_LIST[1][1](has_and)]
        first_line = [LEXICAL_LIST[0][1](LEXICAL_LIST[verse_num][0])]
        verse_lines = ", ".join([LEXICAL_LIST[line][1] for line in range(verse_num, 1, -1)])
        verse = "".join(first_line + [verse_lines] + last_line)
        verses.append(verse)
        verse_num += 1
    return verses

