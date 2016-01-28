import random

def mutate(route):
  """Mutates the route by swapping two random cities in the route"""
  loc1, loc2 = random.sample(range(len(route)), 2)
  route[loc1], route[loc2] = route[loc2], route[loc1]

def create_child(parents, mutate_chance = 5):
  """Takes the two parent routes and creates a child from them

  The first parent supplies the random subset, while the second parent
  fills in the rest of the spots. There is also a chance (mutate_chance,
  in per cent) that dictates the probability that the child will be mutated.

  Returns the child route"""

  start, end = random.sample(range(len(parents[0])), 2)
  if start > end:
    start, end = end, start

  child = [None] * (start) + parents[0][start:end] + [None] * (len(parents[0]) - end)

  for i in range(len(child)):
    if child[i] == None:
      for elem in parents[1]:
        if elem not in child:
	  child[i] = elem

  if random.randint(1, 100) <= mutate_chance:
    mutate(child)

  return child

def create_population(population_size, cities):
  """Creates a population(list of routes) of of length population_size from the cities provided
  
  Returns this population"""
  cities_cpy = cities[:]

  population = [None] * population_size
  for i in range(population_size):
    random.shuffle(cities_cpy)
    population[i] = cities_cpy[:]
  
  return population