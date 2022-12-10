from pathlib import Path


class Solution():
    def __init__(self) -> None:
        self.find_top_n_elves = 3
        self.current_elf_number = 1
        self.current_calories_sum = 0
        self.list_of_elves_and_calories: list[dict[str, int]] = []

    def solve(self) -> None:
        with open(f'{Path(__file__).resolve().parent}/day_01_input.txt',
                  encoding='utf-8') as input_file:
            for line in input_file:
                if len(line.strip()) == 0:
                    self.process_next_elf()
                else:
                    self.current_calories_sum += int(line)
            self.process_next_elf()

        self.list_of_elves_and_calories.sort(key=lambda x: x['calories'],
                                             reverse=True)

        total_calories = 0
        for i in range(self.find_top_n_elves):
            print(f'Elf #{self.list_of_elves_and_calories[i]["elf"]} '
                  f'with {self.list_of_elves_and_calories[i]["calories"]} '
                  f'calories')
            total_calories += self.list_of_elves_and_calories[i]["calories"]

        print(f'Total calories carried by the top {self.find_top_n_elves} ' +
              f'elves: {total_calories}')

    def process_next_elf(self) -> None:
        self.list_of_elves_and_calories.append({
            'elf': self.current_elf_number,
            'calories': self.current_calories_sum
        })

        self.current_calories_sum = 0
        self.current_elf_number += 1


Solution().solve()
