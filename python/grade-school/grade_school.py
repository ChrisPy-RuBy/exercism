import collections

class School(object):
    def __init__(self, name):
        self.name = name
        self.grades= set() 

  
    def add(self, student, grade):
      self.grades.add((student, grade))

    def grade(self, n):

      student_tuple = ()

      if len(self.grades) < 1:
        return set()


      student_tuple = ()  
      for student in self.grades:
        if student[1] == n:
          student_tuple += student[0],

      return student_tuple
        
    def sort(self):
      combined_results = collections.OrderedDict()
      list_grades = list(self.grades)
  
      def getItem(item):
        return item[1]

      sorted_by_grade = sorted(list_grades, key=getItem)
      for x in sorted_by_grade:
        try:
          combined_results[x[1]] += x[0],
        except:
          combined_results[x[1]] = x[0], 

      for k, v in combined_results.items():
        sorted(v)
        
      return combined_results


