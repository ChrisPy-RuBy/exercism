class Allergies(object):

    def __init__(self, score):
        self.score = score
  
    def is_allergic_to(self, item):
        

        if self.score == 0:
          return False
        else: 
          total_allergies = self.score 

        allergies =dict (
                        eggs=1,
                        peanuts=2,
                        shellfish=4,
                        strawberries=8,
                        tomatoes=16,
                        chocolate=32,
                        pollen=64,
                        cats=128
                        )

        if (total_allergies - allergies[item]) >= 0:
          return True
        else: 
          return False

    @property
    def lst(self):
      internal_score = self.score

      array = ['eggs','peanuts','shellfish','strawberries','tomatoes','chocolate', 'pollen', 'cats']
      results = []
      # if internal_score == 0:
      #   return results
      # else:
      for index, item in enumerate(array):
        if internal_score == 0:
          break
        elif (2 ** index) == internal_score:
          results.append(item)
          internal_score -= (index ** 2)
        else:
          internal_score -= (index-1 ** 2)
          results.append(array[index-1])
      return results

      