class Allergies(object):

    def __init__(self, score):
        self.score = score

    def is_allergic_to(self, item):

        allegies =dict (
                        eggs=1,
                        peanuts=2,
                        shellfish=4,
                        strawberries=8,
                        tomatoes=16,
                        chocolate=32,
                        pollen=64,
                        cats=128
                        )

        if allegies[item] == self.score:
          return True
        else: 
          return False

    @property
    def lst(self):
        pass