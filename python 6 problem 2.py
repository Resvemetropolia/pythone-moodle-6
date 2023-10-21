import random
def roll_dice(num_sides):
    return random.randint(1, num_sides)
max_number = int(input("Enter the maximum number on the dice: ")
while True:
    result = roll_dice(max_number)
    print(f"Dice roll: {result}")
    if result == max_number:
        break