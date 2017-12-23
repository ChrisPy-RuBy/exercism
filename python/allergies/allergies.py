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
        self.personal_allergies_list = []
  
  
    def is_allergic_to(self, item):
      self.lst
      if item in self.personal_allergies_list:
        return True
      else:
        return False

    @property
    def lst(self):
      score = self.score
      counter = 0
      while True:
          if score > 256:
            if score // (2 ** counter) > 0:
              counter += 1
            else:
              norm = (2 ** (counter-1))
              score = score - norm
              break
          else:
            break

      for i in range(len(self.allergies_list), -1, -1):
        j = (2 ** i)
        if score == 1:
          self.personal_allergies_list.append('eggs')
          break
        elif score // j > 0:
          score -= j
          self.personal_allergies_list.append(self.allergies_list[i])
        else:
          continue

      return self.personal_allergies_list
      