import random

def roll_dice():
    print("🎲 Welcome to the Dice Rolling Simulator!")
    
    # 1. Get user input
    sides = int(input("How many sides does your die have? (e.g., 6, 20): "))
    rolls = int(input("How many times do you want to roll? "))
    
    results = []
    
    # 2. Roll the dice
    print("\nRolling...")
    for _ in range(rolls):
        outcome = random.randint(1, sides)
        results.append(outcome)
    
    # 3. Print basic results
    print(f"\nYour rolls: {results}")
    print(f"Total Sum: {sum(results)}")
    print(f"Average Roll: {sum(results) / rolls:.2f}")

# Run the program
roll_dice()

