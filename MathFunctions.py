
def TumorMortality(populationSize, growthRate, carryCapacity, drug1Mortality, drug2Mortality,
                   drug1Concentration, drug2Concentration, magnitude):
    TMResult = (populationSize * (float(growthRate) * (1 - (populationSize / carryCapacity))
                                  - (float(drug1Mortality) * float(drug1Concentration))
                                  - (float(drug2Mortality) * float(drug2Concentration))
                                  - (magnitude * float(drug1Concentration) * float(drug2Concentration))))
    print(TMResult)

def GFunction(growthRate, populationSize, carryCapacity, heritable, drug1Mortality,
              drug2Mortality, drug1Concentration, drug2Concentration, magnitude):
    GFResult = (float(growthRate) * (1 - (populationSize / (carryCapacity * heritable)))
                   - (float(drug1Mortality) * heritable * float(drug1Concentration)) -
                   (float(drug2Mortality) * heritable * float(drug2Concentration)) -
                   (magnitude * float(drug1Concentration) * float(drug2Concentration)))
    print(GFResult)

def LinearTradeoff(drug1Investment): # this function can accommodate either drug
    LTResult = (1 - float(drug1Investment))
    print(LTResult)

def Drug1Mortality(drug1Resistance, drug1Investment, drug2Investment):
    D1M = (1 / (drug1Resistance + (drug1Investment * drug2Investment)))
    print(D1M)

def Drug2Mortality(drug2Resistance, drug1Investment, drug2Investment, d2IDeriv):
    D2M = (1 / (drug2Resistance + (drug1Investment * d2IDerivative * drug2Investment)))
    print(D2M)

if __name__ == "__main__": # All values currently shown below are just test values.
                           # I don't know which of these will actually be decimals.
    TumorMortality(100,0.5,10,0.2,0.3,0.5,0.5,1)
    GFunction(0.5,100,10,1,0.2,0.3,0.5,0.5,1)
    LinearTradeoff(0.3)
    # Not gonna bother running the last two functions. Program shows they run
    # just fine.
    
