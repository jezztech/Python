# Hosted at http://github.com/jezztech/Python/
import random  # Include the random module

def RollDice(min, max): # Define a function
  return random.randint(min,max) # Return a random int with min and max being arguments

print("This is a program to roll a dice.")
print() # Leaves a line
min = int(input("What do you want your minimum to be? ")) # Sets min to the input
max = int(input("What do you want your maximum to be? ")) # Sets max to the input

print("Your randomly generated number is " + str(RollDice(min, max)) + ".") # Output the result of the DiceRoll Function
                                                                            # with min and max as arguments
