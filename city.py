from math import hypot

def total_distance(route):
  """Calculates the total distance taken by the route"""
  d = 0
  for i in range(len(route) - 1):
    d += distance(route[i], route[i + 1])

  return d

def distance(a, b):
  """Returns the distance between two cities, a and b"""
  return hypot(a.x - b.x, a.y - b.y)

class city:
  def __init__(self, (x, y)):
    """Initializes the city"""
    self.x = x
    self.y = y
