from pathlib import Path


def main() -> None:
    total_points = 0
    group: list[str] = []
    with open(f'{Path(__file__).resolve().parent}/day_03_input.txt',
              encoding='utf-8') as input_file:
        for line in input_file:
            if len(group) == 3:
                total_points += get_points_for_group(group)
                group = []

            group.append(line.strip())

        total_points += get_points_for_group(group)

    print(f'Total Points: {total_points}')


def get_points_for_group(group: list[str]) -> int:
    return get_points_for_intersecting_item(list(set(group[0]) & set(group[1])
                                                 & set(group[2]))[0])


def get_points_for_intersecting_item(item: str) -> int:
    possible_value = ord(item) - ord('a') + 1

    if possible_value < 0:
        return ord(item) - ord('A') + 27

    return possible_value


main()
