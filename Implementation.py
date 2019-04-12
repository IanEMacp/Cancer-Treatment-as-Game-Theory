
import random as r

class Cell:
    mortality = 100
    
class Tumor:

  def __init__(self, initialPopulation, carryCapacity=100, growthRate=10):
        self.carryCapacity = carryCapacity
        self.population = initialPopulation
        self.growthRate = growthRate

  def Mortality(self, drug1Mortality, drug2Mortality,
                       drug1Concentration, drug2Concentration, magnitude):
        TMResult = (population.size() * (float(self.growthRate) * (1 - (population.size() / self.carryCapacity))
                                      - (float(drug1Mortality) * float(drug1Concentration))
                                      - (float(drug2Mortality) * float(drug2Concentration))
                                      - (magnitude * float(drug1Concentration) * float(drug2Concentration))))
        return TMResult

def GFunction(growthRate, populationSize, carryCapacity, heritable, drug1Mortality,
              drug2Mortality, drug1Concentration, drug2Concentration, magnitude):
    GFResult = (float(growthRate) * (1 - (populationSize / (carryCapacity * heritable)))
                   - (float(drug1Mortality) * heritable * float(drug1Concentration)) -
                   (float(drug2Mortality) * heritable * float(drug2Concentration)) -
                   (magnitude * float(drug1Concentration) * float(drug2Concentration)))
    return GFResult

if __name__ == "__main__": # All values currently shown below are just test values.
                           # I don't know which of these will actually be decimals.
    TumorMortality(100,0.5,10,0.2,0.3,0.5,0.5,1)
    GFunction(0.5,100,10,1,0.2,0.3,0.5,0.5,1)
    LinearTradeoff(0.3)
    # Not gonna bother running the last two functions. Program shows they run
    # just fine.
    
