from pathlib import Path

# A for Rock, B for Paper, and C for Scissors
# X => lose, Y => draw, Z => win
# Points: 1 for Rock (X), 2 for Paper (Y), and 3 for Scissors (Z)
# Points: 0 if you lost, 3 if the round was a draw, and 6 if you won


possible_points = {
    'A X': 0 + 3,
    'A Y': 3 + 1,
    'A Z': 6 + 2,
    'B X': 0 + 1,
    'B Y': 3 + 2,
    'B Z': 6 + 3,
    'C X': 0 + 2,
    'C Y': 3 + 3,
    'C Z': 6 + 1,
}

with open(f'{Path(__file__).resolve().parent}/day_02_input.txt',
          encoding='utf-8') as input_file:
    points = [possible_points[line.strip()] for line in input_file]

print(f'Total Points: {sum(points)}')
