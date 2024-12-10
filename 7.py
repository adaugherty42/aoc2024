from itertools import product
import re

equations = []

with open('inputs/day7') as fp:
    for line in fp.read().split('\n'):
        if line:
            regex = re.match(r'([0-9]+): (.+)', line)
            equations.append({'target': int(regex.group(1)), 'operands': [int(x) for x in regex.group(2).split()]})

def merge_ints(int1, int2):
    return int(str(int1) + str(int2))

def apply_operator(int1, int2, operator):
    if operator == '__merge__':
        return merge_ints(int1, int2)
    else:
        return getattr(int1, operator)(int2)

# part 1
operators = ['__add__', '__mul__']
test_value_sum = 0

for equation in equations:
    operands = equation['operands']
    op_orderings = list(product(operators, repeat=len(operands)-1))
    
    for ordering in op_orderings:
        res = getattr(operands[0], ordering[0])(operands[1])
        for j in range(1, len(ordering)):
            res = getattr(res, ordering[j])(operands[j + 1])
        if res == equation['target']:
            test_value_sum += res
            break


print(f'part 1: {str(test_value_sum)}')

# part 2
operators = ['__add__', '__mul__', '__merge__']
test_value_sum = 0

for equation in equations:
    operands = equation['operands']
    op_orderings = list(product(operators, repeat=len(operands)-1))
    
    for ordering in op_orderings:
        res = apply_operator(operands[0], operands[1], ordering[0])
        for j in range(1, len(ordering)):
            res = apply_operator(res, operands[j + 1], ordering[j])
        if res == equation['target']:
            test_value_sum += res
            break

print(f'part 2: {str(test_value_sum)}')