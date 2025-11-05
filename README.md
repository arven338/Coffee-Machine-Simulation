# Coffee Machine Simulation

A simple Python simulation of a coffee machine that manages water, coffee beans, sugar, and milk resources. This project demonstrates object-oriented programming concepts, including class creation, state management, and method interaction.

## Features
- **Coffee-Machine Class**: Simulates a basic coffee machine with adjustable resource levels.
- **Resource Tracking**: Tracks amounts of water, coffee beans, sugar, and milk.
- **Power Control**: Methods to enable (`launch`) and disable (`disable`) the machine.
- **Coffee Preparation**: Simulates the process of making coffee with a small delay to mimic brewing.
- **User-Friendly Output**: Displays machine status and remaining resources.

## Requirements
- Python 3.6+

No external dependencies.

## Installation
Clone the repository:
```bash
git clone https://github.com/arven338/Coffee-Machine-Simulation.git
cd Coffee-Machine-Simulation
```

## Usage

### Demo
You can run a test script to check the module's operation:
```bash
python3 demo.py
```

Example output:
```Python
Coffee-machine status:
 Water: 5.0
 Coffee beans: 7.1
 Sugar: 2.1
 Milk: 0.0
 Status: 0

Device successfully enabled!
Making Latte...
Device disabled.

Coffee-machine status:
 Water: 4.5
 Coffee beans: 6.8
 Sugar: 1.9
 Milk: 0.0
 Status: 0
```

### Example Code
```Python
# Comments are in the demo.py file
from coffee_counter import CoffeeMachine

coffee = CoffeeMachine(water=5.0, coffee_beans=7.1, sugar=2.1)
print(coffee)

coffee.launch()
coffee.make_coffee("Latte")
coffee.disable()

print(coffee)
```

