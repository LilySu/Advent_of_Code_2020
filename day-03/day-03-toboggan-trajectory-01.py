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
        if idx > len(ele):
            num_iterations_multiply = (idx // len(ele)) + 1
            input[ix] = input[ix] * num_iterations_multiply

        if input[ix][idx] == "#":
            # string[:position] + character + string[position+1:]
            l.append(input[ix][:idx] + "X" + input[ix][idx + 1 :])
            counter += 1
            if idx != len(input[0]):
                idx += 3
        else:
            # otherwise O
            l.append(input[ix][:idx] + "O" + input[ix][idx + 1 :])
            if idx != len(input[0]):
                idx += 3

    l = "\n".join(l)
    print(l)
    return counter


if __name__ == "__main__":
    print(solve(input))
