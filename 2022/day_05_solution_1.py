"""
[F]         [L]     [M]
[T]     [H] [V] [G] [V]
[N]     [T] [D] [R] [N]     [D]
[Z]     [B] [C] [P] [B] [R] [Z]
[M]     [J] [N] [M] [F] [M] [V] [H]
[G] [J] [L] [J] [S] [C] [G] [M] [F]
[H] [W] [V] [P] [W] [H] [H] [N] [N]
[J] [V] [G] [B] [F] [G] [D] [H] [G]
 1   2   3   4   5   6   7   8   9
"""

stacks = [
    ['J', 'H', 'G', 'M', 'Z', 'N', 'T', 'F'],
    ['V', 'W', 'J'],
    ['G', 'V', 'L', 'J', 'B', 'T', 'H'],
    ['B', 'P', 'J', 'N', 'C', 'D', 'V', 'L'],
    ['F', 'W', 'S', 'M', 'P', 'R', 'G'],
    ['G', 'H', 'C', 'F', 'B', 'N', 'V', 'M'],
    ['D', 'H', 'G', 'M', 'R'],
    ['H', 'N', 'M', 'V', 'Z', 'D'],
    ['G', 'N', 'F', 'H']
]


def move(amount: int, from_stack: int, to_stack: int) -> None:
    """Move a number of blocks from one stack to another."""
    for _ in range(amount):
        stacks[to_stack - 1].append(stacks[from_stack - 1].pop())


move(6, 4, 3)
move(5, 8, 9)
move(1, 4, 5)
move(1, 4, 5)
move(2, 2, 7)
move(2, 1, 6)
move(9, 6, 1)
move(12, 3, 5)
move(1, 8, 4)
move(3, 1, 5)
move(1, 6, 7)
move(10, 5, 2)
move(14, 5, 1)
move(8, 7, 9)
move(11, 2, 9)
move(1, 3, 9)
move(11, 1, 5)
move(2, 1, 9)
move(1, 4, 8)
move(6, 1, 5)
move(1, 8, 3)
move(16, 5, 1)
move(4, 1, 3)
move(1, 5, 6)
move(4, 3, 4)
move(1, 6, 7)
move(21, 9, 6)
move(2, 1, 9)
move(2, 4, 9)
move(5, 9, 4)
move(9, 1, 6)
move(6, 4, 6)
move(1, 6, 2)
move(1, 7, 6)
move(1, 3, 2)
move(8, 6, 9)
move(3, 1, 8)
move(1, 2, 1)
move(13, 6, 3)
move(1, 1, 9)
move(2, 1, 6)
move(3, 8, 4)
move(4, 4, 9)
move(3, 1, 3)
move(22, 9, 8)
move(1, 2, 9)
move(6, 8, 9)
move(15, 6, 5)
move(5, 8, 9)
move(11, 9, 8)
move(13, 5, 1)
move(1, 6, 5)
move(1, 9, 3)
move(21, 8, 3)
move(3, 5, 3)
move(11, 1, 2)
move(25, 3, 1)
move(5, 1, 7)
move(20, 1, 7)
move(1, 6, 7)
move(16, 3, 9)
move(8, 9, 6)
move(1, 1, 5)
move(5, 9, 4)
move(2, 2, 1)
move(2, 9, 4)
move(1, 9, 4)
move(1, 8, 4)
move(1, 5, 2)
move(3, 4, 6)
move(1, 4, 7)
move(9, 7, 6)
move(5, 4, 6)
move(7, 7, 2)
move(1, 1, 6)
move(11, 2, 5)
move(10, 5, 1)
move(1, 6, 8)
move(1, 5, 7)
move(24, 6, 1)
move(12, 1, 4)
move(12, 4, 8)
move(2, 2, 7)
move(3, 7, 2)
move(5, 2, 8)
move(9, 8, 9)
move(9, 8, 5)
move(1, 9, 1)
move(14, 1, 8)
move(11, 7, 9)
move(4, 1, 3)
move(7, 1, 2)
move(3, 3, 7)
move(12, 9, 7)
move(8, 7, 2)
move(4, 9, 2)
move(1, 3, 6)
move(5, 5, 9)
move(14, 2, 1)
move(8, 9, 4)
move(6, 4, 5)
move(5, 5, 7)
move(1, 8, 2)
move(2, 4, 6)
move(4, 7, 3)
move(10, 8, 4)
move(2, 3, 6)
move(7, 7, 6)
move(10, 4, 8)
move(5, 1, 6)
move(8, 2, 1)
move(7, 6, 8)
move(9, 6, 5)
move(16, 1, 6)
move(2, 3, 9)
move(1, 7, 4)
move(2, 9, 1)
move(14, 6, 7)
move(1, 6, 3)
move(2, 6, 3)
move(9, 5, 7)
move(3, 1, 6)
move(3, 3, 7)
move(5, 5, 9)
move(3, 6, 2)
move(1, 6, 2)
move(12, 8, 2)
move(5, 2, 1)
move(2, 1, 3)
move(25, 7, 1)
move(1, 4, 6)
move(2, 3, 9)
move(26, 1, 9)
move(2, 1, 8)
move(1, 6, 8)
move(1, 7, 1)
move(7, 8, 1)
move(7, 1, 5)
move(1, 1, 2)
move(2, 8, 6)
move(32, 9, 8)
move(1, 6, 5)
move(5, 2, 9)
move(1, 9, 7)
move(24, 8, 3)
move(1, 6, 9)
move(3, 2, 5)
move(1, 7, 9)
move(4, 9, 3)
move(8, 8, 7)
move(18, 3, 7)
move(20, 7, 8)
move(6, 8, 9)
move(6, 5, 1)
move(8, 9, 4)
move(3, 5, 4)
move(8, 8, 4)
move(2, 5, 2)
move(3, 1, 5)
move(4, 3, 7)
move(6, 2, 9)
move(3, 3, 6)
move(6, 4, 5)
move(2, 6, 3)
move(1, 3, 1)
move(4, 3, 8)
move(8, 4, 3)
move(4, 3, 7)
move(4, 4, 5)
move(4, 9, 5)
move(3, 3, 4)
move(3, 4, 9)
move(1, 1, 4)
move(2, 1, 5)
move(7, 7, 8)
move(4, 7, 4)
move(1, 6, 7)
move(1, 1, 5)
move(1, 3, 8)
move(11, 5, 9)
move(17, 9, 8)
move(13, 8, 4)
move(1, 4, 8)
move(4, 7, 1)
move(4, 8, 3)
move(6, 5, 4)
move(3, 3, 6)
move(2, 1, 9)
move(1, 9, 5)
move(1, 3, 5)
move(5, 5, 9)
move(2, 1, 8)
move(21, 8, 6)
move(2, 8, 4)
move(4, 9, 6)
move(1, 9, 7)
move(19, 4, 1)
move(28, 6, 5)
move(7, 4, 2)
move(28, 5, 3)
move(1, 9, 4)
move(1, 4, 2)
move(1, 7, 8)
move(1, 8, 9)
move(13, 1, 3)
move(8, 2, 8)
move(3, 1, 2)
move(5, 8, 5)
move(1, 2, 7)
move(1, 9, 7)
move(1, 2, 3)
move(2, 7, 9)
move(1, 2, 6)
move(1, 9, 1)
move(9, 3, 9)
move(3, 9, 1)
move(1, 6, 8)
move(21, 3, 7)
move(7, 9, 4)
move(2, 4, 2)
move(1, 8, 6)
move(7, 1, 4)
move(7, 7, 8)
move(4, 5, 9)
move(10, 7, 1)
move(7, 3, 9)
move(1, 7, 9)
move(1, 5, 3)
move(3, 3, 5)
move(10, 4, 2)
move(1, 3, 7)
move(2, 4, 9)
move(3, 9, 1)
move(3, 7, 1)
move(1, 6, 4)
move(1, 1, 2)
move(1, 3, 4)
move(2, 4, 3)
move(1, 7, 4)
move(4, 8, 9)
move(1, 4, 9)
move(3, 1, 9)
move(12, 1, 7)
move(2, 9, 5)
move(12, 9, 7)
move(5, 5, 1)
move(1, 8, 5)
move(4, 1, 4)
move(1, 9, 6)
move(1, 3, 4)
move(3, 8, 3)
move(1, 1, 7)
move(8, 2, 5)
move(2, 8, 1)
move(10, 7, 1)
move(4, 9, 5)
move(2, 5, 8)
move(11, 5, 4)
move(6, 7, 2)
move(2, 2, 1)
move(1, 7, 5)
move(1, 5, 1)
move(2, 4, 8)
move(1, 6, 9)
move(8, 4, 3)
move(8, 1, 7)
move(7, 1, 2)
move(4, 3, 9)
move(1, 9, 6)
move(7, 2, 1)
move(5, 2, 3)
move(2, 7, 8)
move(5, 8, 4)
move(2, 9, 3)
move(1, 8, 1)
move(6, 3, 5)
move(10, 3, 1)
move(3, 5, 3)
move(3, 2, 1)
move(1, 5, 4)
move(6, 4, 5)
move(1, 6, 2)
move(3, 4, 7)
move(1, 9, 4)
move(2, 3, 1)
move(1, 9, 8)
move(1, 3, 7)
move(4, 4, 8)
move(2, 7, 4)
move(8, 5, 9)
move(2, 8, 6)
move(2, 4, 3)
move(2, 3, 4)
move(4, 9, 7)
move(1, 8, 7)
move(2, 6, 9)
move(2, 8, 9)
move(1, 2, 9)
move(1, 7, 8)
move(1, 2, 7)
move(19, 7, 6)
move(1, 8, 1)
move(2, 4, 8)
move(5, 6, 1)
move(2, 7, 2)
move(2, 2, 8)
move(2, 1, 8)
move(4, 8, 2)
move(3, 2, 8)
move(6, 9, 5)
move(8, 6, 3)
move(26, 1, 6)
move(1, 5, 3)
move(1, 1, 5)
move(8, 3, 1)
move(1, 3, 7)
move(3, 9, 2)
move(4, 2, 6)
move(26, 6, 1)
move(1, 7, 5)
move(3, 8, 4)
move(2, 8, 2)
move(7, 1, 2)
move(1, 5, 9)
move(2, 4, 6)
move(9, 6, 2)
move(18, 1, 7)
move(6, 7, 1)
move(6, 5, 6)
move(1, 1, 2)
move(19, 2, 7)
move(1, 4, 2)
move(9, 7, 1)
move(3, 6, 7)
move(1, 9, 4)
move(1, 2, 3)
move(8, 7, 8)
move(4, 6, 5)
move(2, 6, 3)
move(1, 4, 2)
move(4, 5, 1)
move(8, 8, 7)
move(17, 7, 8)
move(3, 3, 1)
move(1, 2, 8)
move(8, 8, 4)
move(8, 8, 7)
move(1, 8, 2)
move(7, 7, 6)
move(1, 2, 7)
move(5, 7, 8)
move(7, 1, 6)
move(10, 6, 1)
move(4, 7, 9)
move(3, 9, 7)
move(1, 7, 2)
move(6, 4, 2)
move(7, 1, 5)
move(4, 2, 5)
move(16, 1, 9)
move(3, 2, 7)
move(2, 4, 9)
move(4, 1, 6)
move(5, 7, 4)
move(4, 6, 3)
move(1, 7, 4)
move(1, 6, 9)
move(1, 8, 5)
move(4, 3, 2)
move(2, 5, 3)
move(3, 6, 2)
move(3, 2, 1)
move(9, 5, 8)
move(1, 3, 1)
move(10, 8, 1)
move(1, 8, 5)
move(16, 9, 2)
move(1, 3, 2)
move(12, 1, 9)
move(1, 9, 2)
move(3, 1, 6)
move(2, 1, 9)
move(3, 6, 8)
move(20, 2, 7)
move(16, 9, 7)
move(1, 7, 5)
move(2, 5, 9)
move(2, 2, 3)
move(2, 8, 5)
move(3, 9, 7)
move(2, 5, 2)
move(1, 4, 6)
move(2, 1, 4)
move(23, 7, 5)
move(4, 8, 5)
move(7, 7, 1)
move(16, 5, 7)
move(1, 6, 5)
move(1, 2, 4)
move(2, 3, 9)
move(1, 2, 3)
move(13, 5, 1)
move(1, 3, 8)
move(1, 9, 4)
move(19, 1, 9)
move(2, 1, 9)
move(22, 9, 8)
move(14, 8, 5)
move(12, 5, 3)
move(21, 7, 9)
move(14, 9, 7)
move(1, 8, 6)
move(9, 3, 7)
move(1, 3, 2)
move(4, 4, 1)
move(1, 2, 4)
move(1, 3, 9)
move(6, 8, 9)
move(4, 1, 7)
move(2, 5, 9)
move(6, 4, 5)
move(4, 7, 4)
move(1, 5, 3)
move(5, 9, 7)
move(2, 3, 1)
move(6, 9, 6)
move(1, 1, 6)
move(2, 4, 2)
move(8, 7, 5)
move(20, 7, 5)
move(2, 5, 6)
move(4, 9, 5)
move(1, 1, 3)
move(1, 3, 4)
move(1, 2, 7)
move(1, 4, 9)
move(9, 6, 3)
move(2, 4, 3)
move(28, 5, 3)
move(1, 8, 3)
move(1, 8, 1)
move(1, 2, 8)
move(1, 6, 2)
move(1, 8, 1)
move(6, 5, 7)
move(1, 5, 1)
move(1, 9, 2)
move(1, 1, 3)
move(1, 9, 7)
move(2, 1, 2)
move(11, 3, 8)
move(3, 8, 6)
move(3, 6, 9)
move(25, 3, 7)
move(4, 3, 8)
move(4, 2, 3)
move(9, 8, 9)
move(2, 3, 7)
move(3, 8, 2)
move(11, 9, 7)
move(1, 9, 1)
move(4, 7, 3)
move(1, 1, 5)
move(23, 7, 2)
move(12, 2, 3)
move(2, 3, 9)
move(12, 2, 1)
move(2, 3, 9)
move(1, 5, 4)
move(1, 2, 5)
move(1, 9, 4)
move(1, 5, 9)
move(2, 4, 2)
move(3, 1, 4)
move(1, 2, 1)
move(10, 3, 2)
move(7, 7, 3)
move(11, 7, 9)
move(5, 3, 1)
move(1, 4, 5)
move(11, 2, 3)
move(9, 9, 3)
move(3, 9, 4)
move(2, 4, 8)
move(1, 5, 6)
move(13, 1, 5)
move(3, 3, 8)
move(3, 7, 2)
move(1, 7, 4)
move(3, 8, 3)
move(8, 3, 8)
move(4, 4, 5)
move(2, 8, 2)
move(8, 8, 3)
move(1, 6, 3)
move(2, 2, 8)
move(6, 5, 2)
move(3, 2, 8)
move(1, 1, 7)
move(2, 9, 3)
move(3, 5, 4)
move(2, 8, 6)

# print top of each stack
for s in stacks:
    print(s[-1])
