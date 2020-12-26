from typing import List

from run_for_all_input_and_timer import Manager, timer

setup = Manager()
input = setup.get_file()


@timer
class Trajectory:
    """
    prints pattern with X's and O's
    in given slope based on right and down.
    elongates input as needed depending on slope
    """
    def __init__(self, input, right, down):
        self.input = input
        self.right = right
        self.down = down
        self.counter = 0

    # for coordinate at top left
    # decrement to the right
    # check grid storage
    def get_count(self):
        # make a full grid based on slope requirements
        self.input = [(self.input[i] * len(self.input[0])) + self.input[0] for i in range(len(self.input))]
        for item_in_input in range(0, len(self.input[:3]) + 1, self.down):

            for item_in_line in range(0, len(self.input[item_in_input]) + 1, self.right):
                if self.input[item_in_input][item_in_line] == '#':
                    print(self.input[item_in_input][:item_in_line] + 'X' + self.input[item_in_input][item_in_line + 1:])
        #             self.counter += 1
        #             print(item_in_input, item_in_line)
        #             print(self.input[item_in_input])
        # return self.counter
        return self.input
    #
    # def get_length(self, index_of_input):
    #     len(self.input[index_of_input])
    #
    # def check_tree(self):
    #     for ix in range(0, len(self.input), self.down):
    #         for idx in range(len(self.input[ix])):
    #             if self.input[ix][idx] == '#':
    #                 print(self.input[ix][:idx] + 'X' + self.input[ix][idx + 1:])
    #                 self.counter += 1
    #             else:
    #                 print(self.input[ix][:idx] + 'O' + self.input[ix][idx + 1:])
    #
    # def make_pattern_longer(self):
    #     idx = 0
    #     # for each item in list
    #     for ix, ele in enumerate(self.input):
    #         if idx > len(ele):
    #             num_iterations_multiply = (idx // len(ele)) + 1
    #             self.input[ix] = self.input[ix] * num_iterations_multiply
    #
    #         if idx != len(self.input[0]):
    #             idx += self.right


# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.
# multiply together

# 184


if __name__ == "__main__":
    t = Trajectory(input, 3, 1)
    print(len(t.get_count()))
