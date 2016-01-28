from math import hypot

def distance(a, b):
  """Returns the distance between two cities, a and b"""
  return hypot(a.x - b.x, a.y - b.y)

class city:
  def __init__(self, (x, y)):
    """Initializes the city"""
    self.x = x
    self.y = y
