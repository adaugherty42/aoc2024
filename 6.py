board = []

with open('inputs/day6') as fp:
    for line in fp.read().split('\n'):
        if line:
            board.append(list(line))

ROWS, COLS = len(board), len(board[0])

def find_starting_coords():
    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] == '^': return (j, i)

def change_direction(curr_direction):
    if curr_direction == 'north': return 'east'
    if curr_direction == 'east': return 'south'
    if curr_direction == 'south': return 'west'
    if curr_direction == 'west': return 'north'

def get_new_coords(coords, direction):
    (x, y) = coords
    if direction == 'north': return (x, y - 1)
    if direction == 'east': return (x + 1, y)
    if direction == 'south': return (x, y + 1)
    if direction == 'west': return (x - 1, y)

def is_cell_out_of_bounds(x, y):
    return x < 0 or x >= COLS or y < 0 or y >= ROWS

def is_cell_an_obstacle(x, y):
    return board[y][x] == '#'

def traverse(x, y):
    path = set([(x, y)])
    curr_direction = 'north'

    while True:
        (potential_x, potential_y) = get_new_coords((x, y), curr_direction)
        
        if is_cell_out_of_bounds(potential_x, potential_y):
            break
        
        if is_cell_an_obstacle(potential_x, potential_y):
            curr_direction = change_direction(curr_direction)
        else:
            path.add((potential_x, potential_y))
            x, y = potential_x, potential_y

    return len(path)

def can_escape(x, y, obstacle_x, obstacle_y):
    curr_direction = 'north'
    obstacles_encountered = set()

    while True:
        (potential_x, potential_y) = get_new_coords((x, y), curr_direction)

        # we've made it out
        if is_cell_out_of_bounds(potential_x, potential_y):
            return True

        # we're encountering either an existing obstacle, or our proposed obstacle
        if is_cell_an_obstacle(potential_x, potential_y) or \
                (potential_x == obstacle_x and potential_y == obstacle_y):

            # if we've already hit this obstacle facing the same direction, then
            # we necessarily have started a cycle.
            if (potential_x, potential_y, curr_direction) in obstacles_encountered:
                return False
            else:
                obstacles_encountered.add((potential_x, potential_y, curr_direction))
                curr_direction = change_direction(curr_direction)
        else:
            x, y = potential_x, potential_y



# part 1
start_x, start_y = find_starting_coords()
part_1_res = traverse(start_x, start_y)

print(f'part 1: {str(part_1_res)}')

# part 2
valid_obstruction_positions = 0
for i in range(ROWS):
    for j in range(COLS):
        if is_cell_an_obstacle(j, i): continue
        if not can_escape(start_x, start_y, j, i):
            valid_obstruction_positions += 1

print(f'part 2: {str(valid_obstruction_positions)}')