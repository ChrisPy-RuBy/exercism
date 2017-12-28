# Globals for the bearings
# Change the values as you see fit
EAST = None
NORTH = None
WEST = None
SOUTH = None

DIRECTIONS = [NORTH, EAST, SOUTH, WEST] 


class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.coordinates = (x, y)
        self.bearing = bearing


    def turn_right(self):
        index = DIRECTIONS.index(self.bearing)
        new_index = index+1
        self.bearing = DIRECTIONS[new_index]

    def turn_left(self):
        index = DIRECTIONS.index(self.bearing)
        new_index = index-1
        self.bearing = DIRECTIONS[new_index]       


robot = Robot()
print (robot.bearing)
robot.turn_right()
print (robot.bearing)
  