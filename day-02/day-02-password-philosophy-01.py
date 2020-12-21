import re
from collections import Counter
from typing import List

from run_for_all_input_and_timer import Manager, timer

setup = Manager()
input = setup.get_file()


@timer
def solve(input: List[str]) -> int:
    # set count of correct passwords
    correct_count = 0
    # get each item in list ie. '6-7 q: qqqqvqhq'
    for str_credentials in input:
        before_colon = re.compile(r"^[^:]+:")
        # get a str of everything before colon ie. '6-7 q:'
        [requirement] = before_colon.findall(str_credentials)
        # split number requirement from letter using space ie. ['6-7', 'q']
        requirement_lst = requirement[:-1].split(" ")
        # get a range of numbers on either side of '-' ie. ['6', '7']
        num_range_lst = requirement_lst[0].split("-")
        required_letter = requirement_lst[1]
        # get password ie. 'qqqqvqhq'
        psswd = str_credentials.replace(requirement + " ", "")
        psswd_dict = Counter(psswd)
        for key in psswd_dict:
            if psswd_dict[key] >= int(num_range_lst[0]) and psswd_dict[key] <= int(
                num_range_lst[1]
            ):
                print(
                    psswd,
                    required_letter,
                    num_range_lst,
                )
                correct_count += 1
    return correct_count


if __name__ == "__main__":
    print(solve(input))
