import random

def mutate(route):
  """Mutates the route by swapping two random cities in the route"""
  loc1, loc2 = random.sample(range(len(route)), 2)
  route[loc1], route[loc2] = route[loc2], route[loc1]