with open('input.txt', 'r') as f:
    data = f.read().splitlines()

# with open('sample_input.txt', 'r') as f:
#     data = f.read().splitlines()

octopuses = []
flashed = []


for string in data:
    entry = []
    for char in string:
        entry.append(int(char))

    octopuses.append(entry)


def get_coords_adjacent_octopi(row: int, col: int) -> int:

    offsets = ((-1, 0), (-1, +1), (0, +1), (+1, +1), (+1, 0), (+1, -1), (0, -1), (-1, -1))

    adjacent_octopi = []

    for row_offset, col_offset in offsets:

        row_val = row+row_offset
        col_val = col+col_offset

        if col_val < 0 or col_val >= len(data[0]) or row_val < 0 or row_val >= len(data[0]):
            continue

        adjacent_octopi.append((row_val, col_val))
        
    return adjacent_octopi



def check_should_flash(row, col):
    try:
        index = flashed.index((row, col))

    except ValueError:
        index = -1

    if octopuses[row][col] > 9 and index < 0:
        flash(row, col)



def flash(row, col):
    flashed.append((row, col))

    adjacent_octopi = get_coords_adjacent_octopi(row, col)

    for adj_row, adj_col in adjacent_octopi:
        if (adj_row, adj_col) not in flashed:
            octopuses[adj_row][adj_col] += 1

            check_should_flash(adj_row, adj_col)



def step():
    #increment every octopi's value
    for row_num, row in enumerate(octopuses):
        for col_num, val in enumerate(row):
            octopuses[row_num][col_num] += 1

    
    #make octopi flash if val > 9
    for row_num, row in enumerate(octopuses):
        for col_num, val in enumerate(row):

            if check_should_flash(row_num, col_num):

                flash(row_num, col_num)

                adjacent_octopi = get_coords_adjacent_octopi(row_num, col_num)

                for adj_row, adj_col in adjacent_octopi:
                    if (adj_row, adj_col) not in flashed:
                        octopuses[adj_row][adj_col] += 1


    for row, col in flashed:
        octopuses[row][col] = 0

    num_flashed = len(flashed)
    flashed.clear()

    return num_flashed


count = 0
for i in range(100):
    count += step()

    print(f'\n\nstep {i+1}:')
    for x in octopuses:
        print(x)

print(count)
