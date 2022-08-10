from collections import deque

with open('input.txt', 'r') as f:
    data = f.readlines()

# with open('sample_inp.txt', 'r') as f:
#     data = f.readlines()


data = [x.strip('\n') for x in data]

tracked_nums = [[0] * len(data[0]) for _ in range(len(data))]

assert len(tracked_nums) == len(data)

neighbors = (-1, 0), (0, +1), (+1, 0), (0, -1)

def main() -> None:

    #set locations of 9's to -1's in tracked_nums
    set_basin_boundaries(data)

    to_visit = generate_low_points(data, neighbors)


    largest_basins = []
    for coord in to_visit:
        basin_size = len(list(traverse_basin(data, coord)))

        if basin_size < 1:
            continue

        if len(largest_basins) < 3:
            largest_basins.append(basin_size)

        elif basin_size > min(largest_basins):
            min_idx = largest_basins.index(min(largest_basins))
            largest_basins[min_idx] = basin_size


    assert len(largest_basins) == 3
    print(largest_basins[0] * largest_basins[1] * largest_basins[2])
    




def traverse_basin(map: list, start_coord: tuple):
    '''
    yield adjacent locations to start_coord
    that are in the same basin
    '''

    block = {start_coord}
    visit = deque(block)
    child = deque.pop

    while visit:
        node = child(visit)

        for offset in neighbors:
            index = get_next(node, offset)

            if index not in block:
                block.add(index)

                if is_valid(map, index):
                    if tracked_nums[index[0]][index[1]] != -1:
                        visit.append(index)
                    

        if tracked_nums[node[0]][node[1]] != -1:
            tracked_nums[node[0]][node[1]] = -1
            yield node



def generate_low_points(map: list, neighbors: list) -> list:
    
    low_points = []

    for row, i in enumerate(map):
        for col, num in enumerate(i):

            adjacent_numbers = []
            for direction in neighbors:
                row_offset, col_offset = direction

                if is_valid(map, (row+row_offset, col+col_offset)):
                    adjacent_numbers.append(int(map[row+row_offset][col+col_offset]))


            valid_adjacent_nums = [x for x in adjacent_numbers if x != -1]

            if min(valid_adjacent_nums) > int(num):
                low_points.append((row, col))

    return low_points



def set_basin_boundaries(map: list) -> list:
    for row, i in enumerate(map):
        for col, num in enumerate(i):
            if int(num) == 9:
                tracked_nums[row][col] = -1



def get_next(node, offset):
    '''
    Find the next location based on an offset from the current location.
    '''

    row, column = node
    row_offset, column_offset = offset
    return row + row_offset, column + column_offset



def is_valid(array, index):
    '''
    Verify that the index is in range of the data structure's contents.
    '''

    row, column = index
    return 0 <= row < len(array) and 0 <= column < len(array[row])




if __name__ == '__main__':
    main()