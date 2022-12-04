from pathlib import Path

# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
# Points: 1 for Rock (X), 2 for Paper (Y), and 3 for Scissors (Z)
# Points: 0 if you lost, 3 if the round was a draw, and 6 if you won


possible_points = {
    'A X': 1 + 3,
    'A Y': 2 + 6,
    'A Z': 3 + 0,
    'B X': 1 + 0,
    'B Y': 2 + 3,
    'B Z': 3 + 6,
    'C X': 1 + 6,
    'C Y': 2 + 0,
    'C Z': 3 + 3,
}

with open(f'{Path(__file__).resolve().parent}/day_02_input.txt',
          encoding='utf-8') as input_file:
    points = [possible_points[line.strip()] for line in input_file]

print(f'Total Points: {sum(points)}')
