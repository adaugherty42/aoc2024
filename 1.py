from collections import Counter, defaultdict

list1, list2 = [], []

with open("inputs/day1") as fp:
    for line in fp.read().split('\n'):
        contents = line.split()
        if len(contents) < 2: continue

        list1.append(int(contents[0]))
        list2.append(int(contents[1]))

# part 1
list1.sort()
list2.sort()

delta = 0

for i in range(len(list1)):
    delta += abs(list1[i] - list2[i])

print(f'part 1: {str(delta)}')

# part 2
frequencies = defaultdict(int, Counter(list2))
res = sum([x * frequencies[x] for x in list1])
print(f'part 2: {str(res)}')