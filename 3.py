import re

# part 1
with open('inputs/day3') as fp:
    raw_instructions = re.findall(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)', fp.read())
    res = sum([int(x) * int(y) for (x,y) in raw_instructions])
    print(f'part 1: {str(res)}')

# part 2
with open('inputs/day3') as fp:
    raw_instructions = re.findall(r'(do\(\))|(don\'t\(\))|mul\(([0-9]{1,3}),([0-9]{1,3})\)', fp.read())
    is_enabled = True
    sum_of_products = 0

    for instruction in raw_instructions:
        if instruction[0] == 'do()':
            is_enabled = True
        elif instruction[1] == 'don\'t()':
            is_enabled = False
        elif is_enabled:
            product = int(instruction[2]) * int(instruction[3])
            sum_of_products += product

    print(f'part 2: {str(sum_of_products)}')