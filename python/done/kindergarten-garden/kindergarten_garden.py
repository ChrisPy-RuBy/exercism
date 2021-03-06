class Garden(object):
    def __init__(self, diagram, students=['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet','Ileana', 'Joseph', 'Kincaid', 'Larry']):
        self.diagram = diagram
        self.values_dict = {
          "R": "Radishes",
          "C": "Clover",
          "G": 'Grass',
          "V": "Violets"
        }
        # dont understand why you can't sort alphabetically here!
        self.students = students

    def parse_diagram(self):
      split_diagram = self.diagram.split("\n")
      return split_diagram

    def plants(self, student):

      students_plants = []

      students = self.students.sort()
      
      if student in self.students:
        student_index = self.students.index(student)
      values = (student_index * 2), (student_index * 2 + 1)


      split_diagram = self.parse_diagram()
      for x in split_diagram:
        for value in values:
          # print (self.values_dict.get(x[value]))
          students_plants.append(self.values_dict.get(x[value]))
      return students_plants


      





        

      


 