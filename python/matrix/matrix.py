class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = self.generatematrix(matrix_string)

    def generatematrix(self, matric_string):
        return [x.split(' ') for x in matric_string.split('\n')]

    def row(self, index):
        row = self.matrix[index]
        return [int(x) for x in row]
    
    def column(self, index):
        column = [a[index] for a in self.matrix]
        return [int(x) for x in column]

