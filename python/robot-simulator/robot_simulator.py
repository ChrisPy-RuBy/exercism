# Globals for the bearings
# Change the values as you see fit
EAST = (1,0)
NORTH = (0,1)
WEST = (-1, 0)
SOUTH = (0,-1)

DIRECTIONS = [NORTH, EAST, SOUTH, WEST] 


class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.coordinates = (x, y)
        self.bearing = bearing


    def turn_right(self):
        index = DIRECTIONS.index(self.bearing)
        
        if index != 3:
          new_index = index+1
        else: 
          new_index = 0
        self.bearing = DIRECTIONS[new_index]

    def turn_left(self):
        index = DIRECTIONS.index(self.bearing)
        if index != 0:
          new_index = index-1
        else:
          new_index = 3
        self.bearing = DIRECTIONS[new_index]    

    def advance(self):
      new_coordinates = (self.coordinates[0] + self.bearing[0], self.coordinates[1] + self.bearing[1] )
      self.coordinates = new_coordinates

    def simulate(self, string):
      instructions = list(string.upper())
      for item in instructions:
        if item == 'A':
          self.advance()
        elif item == 'R':
          self.turn_right()
        elif item == 'L':
          self.turn_left()
        else:
          raise ValueError

robot = Robot(NORTH, 0, 0)

  