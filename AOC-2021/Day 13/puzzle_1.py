from copy import deepcopy

with open('input.txt', 'r') as f:
    data = f.read().splitlines()


# with open('sample_input.txt', 'r') as f:
#     data = f.read().splitlines()

biggest_x, biggest_y = 0, 0
coords = []
folds = []


def fold(map: list, fold_line: str) -> list:
    '''
    Return folded map
    '''

    if fold_line[0] == 'x':
        x_len = len(map[0]) // 2
        y_len = len(map)
        cut = 'x'

    #fold on y line
    else:
        x_len = len(map[0])
        y_len = len(map) // 2
        cut = 'y'

    #maps properly generate
    new_map = [[0] * (x_len) for _ in range((y_len))]
    side_getting_cut = [[0] * (x_len) for _ in range((y_len))]


    for row_num, row in enumerate(new_map):
        for col_num, col in enumerate(row):
            new_map[row_num][col_num] = map[row_num][col_num]

    if cut == 'x':
        for row_num, row in enumerate(side_getting_cut):
            for col_num, col in enumerate(row):
                side_getting_cut[row_num][col_num] = map[row_num][col_num+x_len+1]

    
    elif cut == 'y':
        for row_num, row in enumerate(reversed(side_getting_cut)):
            for col_num, col in enumerate(row):
                
                side_getting_cut[row_num][col_num] = map[row_num+y_len+1][col_num]


    #mirror side getting cut
    mirrored_side = deepcopy(side_getting_cut)

    #set everything to 0s
    for row_num, row in enumerate(mirrored_side):
        for col_num, col in enumerate(row):
            if col == 1:
                mirrored_side[row_num][col_num] = 0

    if cut == 'x':
        for i in range(len(side_getting_cut)):
            for j in range(len(side_getting_cut[0])-1, -1, -1):
                mirrored_side[i][len(side_getting_cut[0])-j-1] = side_getting_cut[i][j]

    if cut == 'y':
        for i in range(len(side_getting_cut)-1, -1, -1):
            for j in range(len(side_getting_cut[0])):
                mirrored_side[len(side_getting_cut)-i-1][j] = side_getting_cut[i][j]



    # for row_num, row in enumerate(side_getting_cut):
    for row_num, row in enumerate(mirrored_side):
        for col_num, col in enumerate(row):
            if col == 1:
                new_map[row_num][col_num] = 1

    return new_map



for line in data:

    if line == '':
        continue

    if line[0] != 'f':

        x, y = line.split(',')
        x, y = int(x), int(y)

        if x > biggest_x:
            biggest_x = x

        if y > biggest_y:
            biggest_y = y
        
        coords.append((x, y))

    else:
        folds.append(line)

map = [[0] * (biggest_x+1) for _ in range((biggest_y+1))]
folds = [x.split(' ')[-1] for x in folds]

for x, y in coords:
    map[y][x] = 1


first_fold = fold(map, folds[0])


count = 0
for row in first_fold:
    for val in row:
        if val >= 1:
            count += 1

print(count)
