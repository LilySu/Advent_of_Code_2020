import re
from typing import List

from run_for_all_input_and_timer import Manager, timer

setup = Manager()
input = setup.get_file()


@timer
def solve(input: List[str]) -> int:

    for seat in input:
        # set a low, middle, high
        row_range = [0, 63, 127]
        row = 0
        col_range = [0, 7]
        col = 0

        for letter in seat[:6]:
            low = row_range[0]
            mid = row_range[1]
            high = row_range[2]
            # higher
            if letter == 'B':
                row_range = [mid, high]
                print(letter)
                print(row_range)
            # lower
            elif letter == 'F':
                row_range = [low, mid]
                print(letter)
                print(row_range)
        if seat[6] == 'B':
            row = row_range[1]
        elif seat[6] == 'F':
            row = row_range[0]
        for letter in seat[-2:-1]:
            low = row_range[0]
            high = row_range[1]
            mid = high // 2
            # lower
            if letter == 'L':
                col_range = [low, mid]
                # print(letter)
                # print(col_range)
            # upper
            elif letter == 'R':
                col_range = [mid, high]
                # print(letter)
                # print(col_range)
        if seat[-1] == 'L':
            col = col_range[0]
        elif seat[-1] == 'R':
            col = col_range[1]
    print(row) # , col)
    # return 0

if __name__ == "__main__":
    # BFFFBBFRRR: row 70, column 7, seat ID 567.
    # FFFBBBFRRR: row14, column 7, seat ID 119.
    # BBFFBBFRLL: row 102, column 4, seat ID 820.
    input = ['BFFFBBFRRR'] # , 'FFFBBBFRRR', 'BBFFBBFRLL']
    print(solve(input))
