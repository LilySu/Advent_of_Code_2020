from typing import List

from run_for_all_input_and_timer import Manager, timer

setup = Manager()
input = setup.get_file()


@timer
def solve(input: List[str], iterate_right: int, iterate_down: int) -> int:
    counter = 0
    l = []
    idx = 0

    # for each item in list
    for ix in range(0, len(input), iterate_down):
        if idx > len(input[ix]):
            num_iterations_multiply = (idx // len(input[ix])) + 1
            input[ix] = input[ix] * num_iterations_multiply
        try:
            if input[ix][idx] == "#":
                # string[:position] + character + string[position+1:]
                l.append(input[ix][:idx] + "X" + input[ix][idx + 1:])
                counter += 1
                if idx != len(input[0]):
                    idx += iterate_right
            else:
                # otherwise O
                l.append(input[ix][:idx] + "O" + input[ix][idx + 1:])
                if idx != len(input[0]):
                    idx += iterate_right
        except:
            pass
    l = "\n".join(l)
    print(l)
    return counter

# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.
# multiply together

# 184


input = open('input-03-sample.txt', r)

if __name__ == "__main__":
    result = solve(input, 1, 1) * solve(input, 3, 1) * solve(input, 5, 1) * solve(input, 7, 1) * solve(input, 1, 2)
    # result = solve(input, 1, 2)
    print(result)
