from string import ascii_lowercase


# with open("fakeinput.txt", "r") as f:
with open("input.txt", "r") as f:
    data = f.readlines()
start, end = (0, 0), (0, 0)

data = [x.strip("\n") for x in data]
heightmap: list[list[int | str]] = []

DIRECTIONS: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited_positions: set[tuple[int, int]] = set()
starting_locs: list[tuple[int, int]] = []


def valid_index(index: tuple[int, int]) -> bool:
    """
    Return whether indices create
    a valid index or not.
    """
    if index[0] < 0 or index[0] >= len(data):
        return False

    if index[1] < 0 or index[1] >= len(data[0]):
        return False

    return True


def get_valid_adjacents(
    index: tuple[int, int],
    visited: list[tuple[int, int]],
    heightmap: list[list[int | str]],
):

    valid_adjacents: list[tuple[int, int]] = []
    height: int | str = heightmap[index[0]][index[1]]

    if height == "S":
        num_height = 1

    elif height == "E":
        num_height = 26

    # otherwise height is already proper number
    else:
        num_height = int(height)

    for direction in DIRECTIONS:
        test_index: tuple[int, int] = (index[0] + direction[0], index[1] + direction[1])

        if test_index in visited:  # do not revisit already visited nodes
            continue

        if valid_index(test_index):
            if test_index not in visited_positions:

                test_height = heightmap[test_index[0]][test_index[1]]
                if test_height == "S":
                    test_height_num = 1

                elif test_height == "E":
                    test_height_num = 26

                else:
                    test_height_num = int(test_height)

                if test_height_num > num_height + 1:
                    continue

                else:
                    valid_adjacents.append(test_index)

    return valid_adjacents


def step_paths(paths: list[list[tuple[int, int]]]) -> list[list[tuple[int, int]]] | int:
    next_paths: list[list[tuple[int, int]]] = []

    for path in paths:
        visited = path[:-1]
        current_pos: tuple[int, int] = path[-1]
        valid_adjacents = get_valid_adjacents(current_pos, visited, heightmap)
        # no valid adjacents
        if not valid_adjacents:
            continue

        else:
            for valid_adjacent in valid_adjacents:
                visited_positions.add(valid_adjacent)
                if heightmap[valid_adjacent[0]][valid_adjacent[1]] == "E":
                    return len(path) + 1

                # path.extend([valid_adjacent])
                next_paths.append(path + [valid_adjacent])

    return next_paths


# transpose chars to height nums unless start/finish letter
for i, row in enumerate(data):
    temp: list[int | str] = []
    for j, letter in enumerate(row):
        if letter == "S" or letter == "E":
            temp.append(letter)

            if letter == "S":
                start = (i, j)
                starting_locs.append(start)

            else:
                end = (i, j)

        else:
            height: int = ascii_lowercase.find(letter) + 1
            if height == 1:
                starting_locs.append((i, j))

            temp.append(height)

    heightmap.append(temp)
    temp = []

path_distances: list[int] = []

for loc in starting_locs:
    paths = []
    visited_positions = set()
    # print(f"on {loc}")

    for valid_adjacent in get_valid_adjacents(loc, [], heightmap):
        paths.append([loc, valid_adjacent])
    while True:
        paths = step_paths(paths)
        if not paths:
            break
        if isinstance(paths, int):
            # minus one to account for starting location being part of list
            path_distances.append(paths - 1)
            break


print(min(path_distances))
