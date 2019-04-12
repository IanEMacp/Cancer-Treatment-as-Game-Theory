
import random as r

class Cell:
  def __init__(self, health = 100, resistence1 = 0, resistence2 = 0, mortalityRate = 20):
        self.health = health
        self.resistence1 = resistence1
        self.resistence2 = resistence2
        self.mortalityRate = mortalityRate

  def age(self):
    self.health = self.health - self.mortalityRate
    return self

  def mutate(self):
    #return mutated cell
    pass

  def reproduce(self):
    #return self w/ or w/o copies
    pass

    
class Tumor:

  def __init__(self, initialPopulation=list(), carryCapacity=100, growthRate=10):
        self.carryCapacity = carryCapacity
        self.population = initialPopulation
        self.growthRate = growthRate

  def age(self):
    self.population = list(map(lambda cell: cell.age(), self.population))

  def reproduce(self):
    self.population = flatten(list(map(lambda cell: cell.reproduce(), self.population)))

  def mutate(self):
    self.population = list(map(lambda cell: cell.mutate(), self.population))


if __name__ == "__main__": # All values currently shown below are just test values.
                           # I don't know which of these will actually be decimals.
    TumorMortality(100,0.5,10,0.2,0.3,0.5,0.5,1)
    GFunction(0.5,100,10,1,0.2,0.3,0.5,0.5,1)
    LinearTradeoff(0.3)
    # Not gonna bother running the last two functions. Program shows they run
    # just fine.
    
