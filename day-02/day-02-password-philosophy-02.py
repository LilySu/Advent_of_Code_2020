from typing import List

from run_for_all_input_and_timer import Manager, timer

setup = Manager()
input = setup.get_file()


@timer
def solve(input: List[str]) -> int:
    input = sorted([int(i) for i in input])
    for idx_i, i in enumerate(input):
        exclude_i = input[idx_i + 1 : :]
        for idx_j, j in enumerate(exclude_i):
            if (2020 - i - j) in input[idx_j + 1 : :]:
                return i * j * (2020 - i - j)


if __name__ == "__main__":
    print(solve(input))
