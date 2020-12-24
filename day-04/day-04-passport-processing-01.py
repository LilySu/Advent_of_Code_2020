import re
from typing import List

from run_for_all_input_and_timer import Manager, timer

setup = Manager()
input = setup.get_file()


@timer
def solve(input: List[str]) -> int:
    counter = 0
    passports = []
    txt_block = []
    req = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    reqc = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    for line in input:
        if line != '':
            if ' ' in line:
                line = line.split(' ')
                for i in line:
                    txt_block.append(i)
            else:
                txt_block.append(line)
        else:
            passports.append(txt_block)
            txt_block = []
    for idx, txt_block in enumerate(passports):
        for idy, field in enumerate(passports[idx]):
            before_colon = re.compile(r"^[^:]+:")
            [requirement] = before_colon.findall(field)
            passports[idx][idy] = requirement[:-1]
    for txt_block in passports:
        if (sorted(txt_block) == sorted(req)) or (sorted(txt_block) == sorted(reqc)):
            counter += 1
    return counter


if __name__ == "__main__":
    print(solve(input))
