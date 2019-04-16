
import random as r
import math as m

class Cell:
  def __init__(self, health = 100, resistence1 = 0, resistence2 = 0, mortalityRate = 20):
        self.health = health
        self.resistence1 = resistence1
        self.resistence2 = resistence2
        self.mortalityRate = mortalityRate

  def age(self):
    if (self.health - self.mortalityRate > 0):
      return Cell(health = self.health - self.mortalityRate, resistence1 = self.resistence1, resistence2 = self.resistence2, mortalityRate = self.mortalityRate)

  def mutate(self):
    change = r.randrange(1, 6, 1)
    if(change == 1):
      return Cell(health = self.health, resistence1 = self.resistence1 + 1, resistence2 = self.resistence2, mortalityRate = self.mortalityRate)
    if(change == 2):
      return Cell(health = self.health, resistence1 = self.resistence1, resistence2 = self.resistence2 + 1, mortalityRate = self.mortalityRate)
    if(change == 3):
      if(self.resistence1 > 0):
        return Cell(health = self.health, resistence1 = self.resistence1 - 1, resistence2 = self.resistence2, mortalityRate = self.mortalityRate)
    if(change == 4):
      if(self.resistence2 > 0):
        return Cell(health = self.health, resistence1 = self.resistence1, resistence2 = self.resistence2 - 1, mortalityRate = self.mortalityRate)
    return Cell(health = self.health, resistence1 = self.resistence1, resistence2 = self.resistence2, mortalityRate = self.mortalityRate)

  def reproduce(self, childHealth):
    oldSelf = Cell(health = self.health, resistence1 = self.resistence1, resistence2 = self.resistence2, mortalityRate = self.mortalityRate)
    rand = r.randrange(1, 6, 1)
    if((rand == 1) or (rand == 2)):
      child = Cell(health = childHealth + 20, resistence1 = self.resistence1, resistence2 = self.resistence2, mortalityRate = self.mortalityRate)
      return [oldSelf, child]
    return [oldSelf]

  def treat(self, drug):
    rand1 = r.randrange(1, 4 + self.resistence1, 1)
    rand2 = r.randrange(1, 4 + self.resistence2, 1)
    if ((drug == 1) & ((rand1) != 1 and (rand1 != 2))):
      return Cell(health = self.health, resistence1 = self.resistence1, resistence2 = self.resistence2, mortalityRate = self.mortalityRate)
    if ((drug == 2) & ((rand2 != 1) and (rand2 != 2))):
      return Cell(health = self.health, resistence1 = self.resistence1, resistence2 = self.resistence2, mortalityRate = self.mortalityRate)
    if (self.health - 40 > 0):
      return Cell(health = self.health - 40, resistence1 = self.resistence1, resistence2 = self.resistence2, mortalityRate = self.mortalityRate)


class Tumor:

  def __init__(self, initialPopulationSize = 100, health = 100, resistence1 = 0, resistence2 = 0, mortalityRate = 20):
        self.childHealth = health
        self.population = list()
        for i in range(1, initialPopulationSize + 1):
          self.population.append(Cell(health - (m.floor(health/5) * m.ceil(i/m.ceil(initialPopulationSize/5)) - m.floor(health/5)), resistence1, resistence2, mortalityRate))

  def age(self):
    self.population = list(filter(None, map(lambda cell: cell.age(), self.population)))

  def reproduce(self):
    self.population = sum(list(map(lambda cell: cell.reproduce(self.childHealth), self.population)), [])

  def mutate(self):
    self.population = list(map(lambda cell: cell.mutate(), self.population))

  def treat(self, drug):
    self.population = list(filter(None, map(lambda cell: cell.treat(drug), self.population)))


def trial(cycles = 13, treatmentStrategy = [], maxTumorSize = 1000, tumorFailureSize = True):
#cycles is the number of 4 week treatment cycles to simulate
#treatmentStrategy must be list containing only 1s and 2s or an empty list for no treatment
  tumor = Tumor()
  for i in range(1, cycles + 1):
    if(treatmentStrategy):
      tumor.treat(treatmentStrategy[i % len(treatmentStrategy)])
    if(len(tumor.population) < maxTumorSize):
      tumor.reproduce()
    tumor.mutate()
    tumor.age()
    if(maxTumorSize < len(tumor.population) and tumorFailureSize):
      print("failed at " + str(i))
      return
  
  print("success: ")
  print("popsize: " + str(len(tumor.population)))
  g = list()
  for x in tumor.population:
    g.append(x.health)
  print("health: " + str(sum(g)/len(g)))
  return len(tumor.population)


def ptrial(cycles = 13, treatmentStrategy = [], maxTumorSize = 1000, tumorFailureSize = True):
#same as trial but with some extra print outs
  tumor = Tumor()
  for i in range(1, cycles + 1):
    print("cycle: " + str(i))
    print("popsize")
    print(len(tumor.population))
    print("health")
    g = list()
    for x in tumor.population:
      g.append(x.health)
    print(sum(g)/len(g))
    if(treatmentStrategy):
      tumor.treat(treatmentStrategy[i % len(treatmentStrategy)])
    if(len(tumor.population) < maxTumorSize):
      tumor.reproduce()
    tumor.mutate()
    tumor.age()
    if(maxTumorSize < len(tumor.population) & tumorFailureSize):
      print("failed at " + str(i))
      return
  print("success")
  print("popsize: " + str(len(tumor.population)))
  g = list()
  for x in tumor.population:
    g.append(x.health)
  print("health: " + str(sum(g)/len(g)))
  return len(tumor.population)

def nptrial(cycles = 13, treatmentStrategy = [], maxTumorSize = 1000, tumorFailureSize = True):
#same as trial but with no print outs
  tumor = Tumor()
  for i in range(1, cycles + 1):
    if(treatmentStrategy):
      tumor.treat(treatmentStrategy[i % len(treatmentStrategy)])
    if(len(tumor.population) < maxTumorSize):
      tumor.reproduce()
    tumor.mutate()
    tumor.age()
    if(maxTumorSize < len(tumor.population) & tumorFailureSize):
      return 1000
  return len(tumor.population)

#print("strat = []:")
#trial(cycles=39)
#print("-----------------------------")
#print("strat = [1]:")
#trial(cycles=39, treatmentStrategy = [1])
#print("-----------------------------")
#print("strat = [1, 2]:")
#trial(cycles=39, treatmentStrategy = [1, 2])
#print("-----------------------------")
#print("strat = [1, 2, 1, 2, 2]:")
#trial(cycles=39, treatmentStrategy = [1, 2, 1, 2, 2])
#print("-----------------------------")

def compareStrats(strat1, strat2):
  #percentage that strat1 is better
  results = list()
  for x in range(1,51):
    if(nptrial(cycles=39, treatmentStrategy = strat1) < nptrial(cycles=39, treatmentStrategy = strat2)):
      results.append(True)
    if(nptrial(cycles=39, treatmentStrategy = strat1) > nptrial(cycles=39, treatmentStrategy = strat2)):
      results.append(False)
  return sum(results)/len(results)

g = list()
for x in range(1,100):
  g.append(nptrial(cycles=39, treatmentStrategy = [1]))
print("+++++++++++++")
print(sum(g)/len(g))
