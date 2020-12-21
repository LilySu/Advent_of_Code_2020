import re
from collections import Counter
from typing import List

from run_for_all_input_and_timer import Manager, timer

setup = Manager()
input = setup.get_file()


@timer
def solve(input: List[str]) -> int:
    counter = 0
    l = []
    idx = 0
    # for each item in list
    for ix, ele in enumerate(input):
        # if #, replace with X,
        if idx == 0 :
            idx = 0
            l.append(ele)
            idx += 3
            continue
        elif idx > len(input[0]):
            break
        elif ele[idx] == '#' and idx <= len(input[0]):
            # string[:position] + character + string[position+1:]
            l.append(ele[:idx] + 'X' + ele[idx + 1:])
            counter += 1
            if idx != len(input[0]):
                idx += 3
        elif idx <= len(input[0]):
            # otherwise O
            l.append(ele[:idx] + 'O' + ele[idx + 1:])
            if idx != len(input[0]):
                idx += 3
        # else:
        #     break
            # idx = 0
        # break
        # check
    l = "\n".join(l)
    print(l)
    # print("\n".join(input))
    return counter


if __name__ == "__main__":
    print(solve(input))
