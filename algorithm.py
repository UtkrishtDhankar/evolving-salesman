import random
import city

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

def evolve_generation(population):
  """Evolves the population by one generation
  Returns the population"""

  # sort the previous generation by their fitness
  population = sorted(population, key=city.total_distance)

  # next_gen is half of the original population, the rest have died off
  next_gen = population[:len(population) / 2]
  # Add in the children of the survivors
  for i in range(0, len(population) / 2, 2):
    next_gen += [
      create_child([population[i], population[i + 1]]),
      create_child([population[i + 1], population[i]])
    ]

  return next_gen

cities = city.read_cities()
population = create_population(16, cities)

for i in range(100):
  population = evolve_generation(population)

best = min(population, key=city.total_distance)
print best
print city.total_distance(best)
