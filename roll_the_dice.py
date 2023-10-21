import random
import re

def roll_dice(num_dice, num_sides):
    if num_dice <= 0 or num_sides <= 0:
        return "Please enter a valid input for the number of dice and sides."

    rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    total = sum(rolls)

    return rolls, total

def parse_expression(expression):
    pattern = r'(\d+)d(\d+)'
    matches = re.findall(pattern, expression)
    results = []

    for match in matches:
        num_dice, num_sides = map(int, match)
        rolls, total = roll_dice(num_dice, num_sides)
        results.append((f"{num_dice}d{num_sides}: {', '.join(map(str, rolls))}", total))

    return results

while True:
    user_input = input("Enter a dice expression or 'exit' to quit: ").strip().lower()

    if user_input == 'exit':
        break

    results = parse_expression(user_input)

    if results:
        for result in results:
            print(result[0], "Total:", result[1])
    else:
        print("Invalid input.  Please use the format 'NdM' (e.g., 2d6) and you can use operators such as +, -, *, or /.")
