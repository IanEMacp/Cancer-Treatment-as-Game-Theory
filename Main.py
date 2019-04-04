#Execute the entire program from this file

#import ModelReplica as MR (or whatever our calculative file is called)

def Main(): #Insert all of our math variable names into the parentheses
    print("How many times?")
    while True:
        try:
            n = int(inpit())
        except ValueError:
            print("Please type a numeric value.")
            print("")
            continue
        else:
            break

    cancerPayoffList = []
    oncologistPayoffList = []

    for x in range(n):
        tumorPayoff, oncologistPayoff, endSituation = MR
