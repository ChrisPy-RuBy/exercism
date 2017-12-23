class Allergies(object):

    def __init__(self, score):
        self.score = score
        self.allergies_list = [ 'eggs',
                        'peanuts',
                        'shellfish',
                        'strawberries',
                        'tomatoes',
                        'chocolate',
                        'pollen',
                        'cats' ]
  
  
    def is_allergic_to(self, item):
      pass
        




    @property
    def lst(self):
      personal_allergies_list = []
      score = self.score
      for i in range(len(self.allergies_list), -1, -1):
        j = (2 ** i)
        if score == 1:
          personal_allergies_list.append('eggs')
          break
        elif score // j > 0:
          score -= j
          print (score)
          personal_allergies_list.append(self.allergies_list[i])
        else:
          continue
      print (personal_allergies_list)
      return personal_allergies_list
      