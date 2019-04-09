
def TumorMortality(populationSize, growthRate, carryCapacity, drug1Mortality, drug2Mortality,
                   drug1Concentration, drug2Concentration, magnitude):
    TMResult = (populationSize * (float(growthRate) * (1 - (populationSize / carryCapacity))
                                  - (float(drug1Mortality) * float(drug1Concentration))
                                  - (float(drug2Mortality) * float(drug2Concentration))
                                  - (magnitude * float(drug1Concentration) * float(drug2Concentration))))
    print(TMResult)
    return TMResult

def GFunction(growthRate, populationSize, carryCapacity, heritable, drug1Mortality,
              drug2Mortality, drug1Concentration, drug2Concentration, magnitude):
    GFResult = (float(growthRate) * (1 - (populationSize / (carryCapacity * heritable)))
                   - (float(drug1Mortality) * heritable * float(drug1Concentration)) -
                   (float(drug2Mortality) * heritable * float(drug2Concentration)) -
                   (magnitude * float(drug1Concentration) * float(drug2Concentration)))
    print(GFResult)
    return GFResult

def stratLinearTradeoff(drugInvestment): # this function can accommodate either drug
    return (1 - float(drug1Investment))

def stratConcaveTradeoff(drugInvestment):
  return (1 - sqrt(1 - (drugInvestment - 1)^2))

def stratConvexTradeoff(drugInvestment):
  return sqrt(1 - drugInvestment^2)

def Drug1Mortality(drug1Resistance, drugInvestment, drugAllocation):
    D1M = (1 / (drug1Resistance + (drugInvestment * drugAllocation)))
    print(D1M)
    return D1M

def Drug2Mortality(drug2Resistance, drugInvestment, drugAllocation, dADerivative):
    D2M = (1 / (drug2Resistance + (drugInvestment * dADerivative * drugAllocation)))
    print(D2M)
    return D2M

def CarryingCapacity([v1, v2], [u1, u2], maxCarryCap, standardVarianceOfGaussianFunction):
  return maxCarryCap^((-v1^2)/(2 * standardVarianceOfGaussianFunction))


if __name__ == "__main__": # All values currently shown below are just test values.
                           # I don't know which of these will actually be decimals.
    TumorMortality(100,0.5,10,0.2,0.3,0.5,0.5,1)
    GFunction(0.5,100,10,1,0.2,0.3,0.5,0.5,1)
    LinearTradeoff(0.3)
    # Not gonna bother running the last two functions. Program shows they run
    # just fine.
    
