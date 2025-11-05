# Import library 
import coffee_counter
from coffee_counter import * # Importing all functions

# Creating object
coffee = CoffeeMachine(water=5.0, coffee_beans=7.1, sugar=2.1) # Setting parameters (adding resources)

print(coffee) # Output the information

coffee.launch() # Let's start the coffee-machine
coffee.make_coffee("Latte") # Let's start making Latte coffee
coffee.disable() # Turn off the coffee-machine

print(coffee) # We display the information again to see how many resources we have left
