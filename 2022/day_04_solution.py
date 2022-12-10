from pathlib import Path


def main() -> None:
    total_contained = 0
    total_overlapping = 0
    with open(f'{Path(__file__).resolve().parent}/day_04_input.txt',
              encoding='utf-8') as input_file:
        for line in input_file:
            if are_sections_totally_contained(line):
                total_contained += 1
            if are_sections_overlapping(line):
                total_overlapping += 1

    print(f'Totally contained sections: {total_contained}')
    print(f'Overlapping sections: {total_overlapping}')


def are_sections_totally_contained(line: str) -> bool:
    ((from1, to1), (from2, to2)) = parse_line(line)
    return from1 <= from2 and to1 >= to2 or from2 <= from1 and to2 >= to1


def are_sections_overlapping(line: str) -> bool:
    ((from1, to1), (from2, to2)) = parse_line(line)
    return not (to1 < from2 or to2 < from1)


def parse_line(line: str) -> tuple[tuple[int, int], tuple[int, int]]:
    (first_section, second_section) = line.strip().split(',')
    return parse_section(first_section), parse_section(second_section)


def parse_section(section: str) -> tuple[int, int]:
    (first_value, second_value) = section.split('-')
    return int(first_value), int(second_value)


main()
