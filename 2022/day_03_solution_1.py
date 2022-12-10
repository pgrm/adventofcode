from pathlib import Path


def main() -> None:
    with open(f'{Path(__file__).resolve().parent}/day_03_input.txt',
              encoding='utf-8') as input_file:
        total_points = sum(get_total_points_for_line(line) for line
                           in input_file)

    print(f'Total Points: {total_points}')


def get_total_points_for_line(line: str) -> int:
    return sum(get_points_for_intersecting_item(item) for item
               in find_intersecting_values_in_item(line))


def find_intersecting_values_in_item(item: str) -> list[str]:
    first_half = set(item[:len(item) // 2])
    second_half = set(item[len(item) // 2:])

    return list(first_half & second_half)


def get_points_for_intersecting_item(item: str) -> int:
    possible_value = ord(item) - ord('a') + 1

    if possible_value < 0:
        return ord(item) - ord('A') + 27

    return possible_value


main()
