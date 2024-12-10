board = []

with open('inputs/day4') as fp:
    for line in fp.read().split('\n'):
        if line:
            board.append(list(line))

ROWS, COLS = len(board), len(board[0])

def is_top(x, y, letter):
    return board[y - 1][x - 1] == letter and board[y - 1][x + 1] == letter

def is_bottom(x, y, letter):
    return board[y + 1][x - 1] == letter and board[y + 1][x + 1] == letter

def is_left(x, y, letter):
    return board[y - 1][x - 1] == letter and board[y + 1][x - 1] == letter

def is_right(x, y, letter):
    return board[y - 1][x + 1] == letter and board[y + 1][x + 1] == letter

def word_search(start_x, start_y, word):
    # base case: we aren't starting with an X
    if board[start_y][start_x] != word[0]: return 0

    num_results = 0

    for delta_x in range(-1, 2):
        for delta_y in range(-1, 2):
            # skip start cell
            if delta_x == start_x and delta_y == start_y: continue
            x, y = start_x, start_y
            rem = word[1:]
            while rem:
                # check board boundaries
                if x + delta_x < 0 or y + delta_y < 0: break
                if x + delta_x >= COLS or y + delta_y >= ROWS: break

                if board[y + delta_y][x + delta_x] == rem[0]:
                    rem = rem[1:]
                    x, y = x + delta_x, y + delta_y
                else:
                    break
            if not rem:
                num_results += 1

    return num_results

def word_search_x(start_x, start_y, middle_letter, outer_letter_1, outer_letter_2):
    if board[start_y][start_x] != middle_letter: return 0

    # can't form X if middle letter is on outer row or col
    if start_x <= 0 or start_x >= COLS - 1: return 0
    if start_y <= 0 or start_y >= ROWS - 1: return 0

    if (is_top(start_x, start_y, outer_letter_1) and is_bottom(start_x, start_y, outer_letter_2)) \
            or (is_top(start_x, start_y, outer_letter_2) and is_bottom(start_x, start_y, outer_letter_1)) \
            or (is_left(start_x, start_y, outer_letter_1) and is_right(start_x, start_y, outer_letter_2)) \
            or (is_left(start_x, start_y, outer_letter_2) and is_right(start_x, start_y, outer_letter_1)):
        return 1

    return 0

# part 1
num_results = 0
for x in range(0, COLS):
    for y in range(0, ROWS):
        num_results += word_search(x, y, 'XMAS')


print(f'part 1: {str(num_results)}')


# part 2
num_results = 0
for x in range(0, COLS):
    for y in range(0, ROWS):
        num_results += word_search_x(x, y, 'A', 'M', 'S')

print(f'part 2: {str(num_results)}')