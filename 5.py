from collections import defaultdict, deque
import re

adjacencies = defaultdict(set)
updates = []

with open('inputs/day5') as fp:
    for line in fp.read().split('\n'):
        ordering_match = re.match(r'([0-9]+)\|([0-9]+)', line)
        if ordering_match is not None:
            (before, after) = ordering_match.groups()
            adjacencies[int(before)].add(int(after))
        elif not line.strip():
            continue
        else:
            updates.append([int(x) for x in line.split(',')])

def in_right_order(update):
    for i in range(0, len(update) - 1):
        if update[i+1] not in adjacencies[update[i]]:
            return False
    return True

def fix_order(update):
    # this is just toposort. start by counting incoming vertices to each node
    incoming = {x: 0 for x in update}

    for i in range(0, len(update)):
        for j in range(0, len(update)):
            if update[j] in adjacencies[update[i]]:
                incoming[update[j]] += 1

    # instantiate queue and add any nodes with no incoming vertices
    q = deque()

    for k, incoming_count in incoming.items():
        if incoming_count == 0:
            q.append(k)

    new_update = []

    while q:
        # whatever comes out of the queue is safe to put in order on our new list
        curr = q.popleft()
        new_update.append(curr)

        # decrement the incoming count of all the nodes connected to this one via an outgoing vertex
        for i in range(len(update)):
            if update[i] in adjacencies[curr]:
                incoming[update[i]] -= 1
                if incoming[update[i]] == 0:
                    q.append(update[i])

    return new_update
    

# part 1
middle_sum = 0
for update in updates:
    if in_right_order(update):
        middle_sum += update[len(update) // 2]

print(f'part 1: {middle_sum}')

# part 2
bad_updates = filter(lambda update: not in_right_order(update), updates)
middle_sum = 0

for update in bad_updates:
    good_update = fix_order(update)
    middle_sum += good_update[len(good_update) // 2]

print(f'part 2: {middle_sum}')