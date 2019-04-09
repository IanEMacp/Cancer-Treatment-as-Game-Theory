# Execute the entire program from this file. This code isn't complete.

import Functions as funct # We need Functions.py for this to run.

def Main(): # Insert all of our used variable names from bottom line
            # into the parentheses.
    print("How many times?")
    while True:
        try:
            n = int(input())
        except ValueError:
            print("Please type a numeric value.") # Error check.
            print("")
            continue
        else:
            break

    cancerPayoffList = []
    oncologistPayoffList = [] 

    for x in range(n): # Game runs for however many times the user says.
        tumorPayoff, oncologistPayoff, endSituation = funct.Game

# Put visual feedback as print statements here.    

# This will run our entire program
Main() # <-- Set variable values into parentheses (ex: 10, 0.5, 20).
       # If variable is user-manipulated, set variable as a string that asks
       # for input.
