# Librares
import time # to simulate work
import random # for random waiting

from time import sleep
from random import uniform

# Coffee-machine class
class CoffeeMachine:
    # Source parameters
    def __init__(self, water=0.0, coffee_beans=0.0, sugar=0.0, milk=0.0):
        self.water = water
        self.coffee_beans = coffee_beans
        self.sugar = sugar
        self.milk = milk
        self.status = 0 # 0 -> disabled, 1 -> enabled.
        
    # Technical information
    def __str__(self):
        return (
            f"Coffee-machine status:\n"
            f" Water: {self.water}\n"
            f" Coffee beans: {self.coffee_beans}\n"
            f" Sugar: {self.sugar}\n"
            f" Milk: {self.milk}\n"
            f" Status: {self.status}\n"
        )

    # Refill function
    def refill(self, water=0.0, coffee_beans=0.0, sugar=0.0, milk=0.0):
        if water >= 0 and coffee_beans >= 0 and sugar >= 0 and milk >= 0:
            self.water += water
            self.coffee_beans += coffee_beans
            self.sugar += sugar
            self.milk += milk
        else:
            pass

    # Launch Coffee-machine logic
    def launch(self):
        if self.status == 1:
            print("Device already turned on!")
        else:
            self.status = 1
            print("Device successfully enabled!")
            
    # Turn off Coffee-machine logic
    def disable(self):
        if self.status == 0:
            print("The device is turned off!")
        else:
            self.status = 0
            print("Device successfully disabled!")
            
    # Make coffee function
    def make_coffee(self, coffee):
        if self.status == 0:
            print("Your device is currently turned off. Turn it on to continue.")
            return
        
        if self.water <= 0.0:
            print("Add water to make coffee!")
            return
        
        if self.coffee_beans <= 0.0:
            print("Add coffee beans to make coffee!")
            return
        
        print(f"Let's start making coffee: {coffee}. Please wait...")
        
        # Resource consumption
        self.water -= 0.2
        self.coffee_beans -= 0.1
        self.milk -= 0.1
        self.sugar -= 0.05
        
        # Work imitation
        time.sleep(random.uniform(10.5, 15.0))
        
        # Finishing up the cooking
        print(f"Your {coffee} is ready. Have a great day!")
