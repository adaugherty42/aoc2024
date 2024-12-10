from collections import defaultdict

antennae = defaultdict(list)

ROWS, COLS = 0, 0

with open('inputs/day8') as fp:
    for i, line in enumerate(fp.read().split('\n')):
        if line:
            ROWS += 1
            # technically we'll set this value over and over but I'm lazy
            COLS = len(line)
            for j, ch in enumerate(list(line)):
                if ch.isalnum():
                    antennae[ch].append((j, i))


def is_cell_out_of_bounds(x, y):
    return x < 0 or x >= COLS or y < 0 or y >= ROWS

antinodes = set()

def check_boundaries_and_maybe_add_antinode(location_1, location_2, factor):
    should_continue = False
    (x_1, y_1), (x_2, y_2) = location_1, location_2

    candidate_1_x = x_1 - factor * (x_2 - x_1)
    candidate_1_y = y_1 - factor * (y_2 - y_1)

    if not is_cell_out_of_bounds(candidate_1_x, candidate_1_y):
        should_continue = True
        antinodes.add((candidate_1_x, candidate_1_y))

    candidate_2_x = x_2 - factor * (x_1 - x_2)
    candidate_2_y = y_2 - factor * (y_1 - y_2)

    if not is_cell_out_of_bounds(candidate_2_x, candidate_2_y):
        should_continue = True
        antinodes.add((candidate_2_x, candidate_2_y))

    return should_continue

# part 1
for _symbol, locations in antennae.items():
    for i in range(len(locations) - 1):
        for j in range(i + 1, len(locations)):
            check_boundaries_and_maybe_add_antinode(locations[i], locations[j], 1)

print(f'part 1: {str(len(antinodes))}')

# part 2
antinodes = set()
for _symbol, locations in antennae.items():
    for i in range(len(locations) - 1):
        for j in range(i + 1, len(locations)):
            antinodes.add((locations[i][0], locations[i][1]))
            antinodes.add((locations[j][0], locations[j][1]))

            factor = 1
            while True:
                if check_boundaries_and_maybe_add_antinode(locations[i], locations[j], factor):
                    factor += 1
                else:
                    break

print(f'part 2: {str(len(antinodes))}')