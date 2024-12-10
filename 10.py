from collections import defaultdict

board = []

with open('inputs/day10') as fp:
    for line in fp.read().split('\n'):
        if line:
            board.append([int(x) for x in list(line.strip())])

matches = defaultdict(set)
paths = defaultdict(list)
ROWS, COLS = len(board), len(board[0])

def is_cell_out_of_bounds(x, y):
    return x < 0 or x >= COLS or y < 0 or y >= ROWS

def backtrack(start_coords, curr_coords, curr_level=0, path=set()):
    if curr_level == 9:
        matches[start_coords].add(curr_coords)
        paths[start_coords].append(path)
        return
    
    (curr_x, curr_y) = curr_coords

    for (delta_x, delta_y) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            candidate_x, candidate_y = curr_x + delta_x, curr_y + delta_y
            if is_cell_out_of_bounds(candidate_x, candidate_y): continue
            if board[candidate_y][candidate_x] != curr_level + 1: continue
            path.add((candidate_x, candidate_y))
            backtrack(start_coords, (candidate_x, candidate_y), curr_level + 1, path)
            path.remove((candidate_x, candidate_y))

for i in range(ROWS):
    for j in range(COLS):
        if board[i][j] == 0:
            backtrack((j, i), (j, i))

print(f'part 1: {str(sum([len(v) for v in matches.values()]))}')
print(f'part 2: {str(sum([len(v) for v in paths.values()]))}')