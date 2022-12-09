with open("input.txt", "r") as f:
    # with open("fakeinput.txt", "r") as f:
    data = f.readlines()


data = [x.strip("\n") for x in data]


def is_tail_adj_head(
    head_coords: tuple[int, int], tail_coords: tuple[int, int]
) -> bool:
    """
    Return True whether tail coords are adjacent to head coords.
    Return False otherwise.
    """

    for i in range(-1, 2):
        for j in range(-1, 2):
            test_coord: tuple[int, int] = (tail_coords[0] + i, tail_coords[1] + j)

            if test_coord == head_coords:
                return True

    return False


OFFSETS: dict[str, tuple] = {"R": (+1, 0), "L": (-1, 0), "U": (0, +1), "D": (0, -1)}

# tail has visited (0, 0) by default, as it starts here
tail_visited: list[tuple[int, int]] = [(0, 0)]
directions: list[tuple[int, int]] = []

# rope head/tails coordinates relative to starting position
head_coords: tuple[int, int] = (0, 0)
tail_coords: tuple[int, int] = (0, 0)

for instruction in data:
    direction, units = instruction.split(" ")
    for i in range(int(units)):
        directions.append((OFFSETS[direction]))

for direction in directions:
    offset = (int(direction[0]), int(direction[1]))
    head_coords = (head_coords[0] + offset[0], head_coords[1] + offset[1])

    if is_tail_adj_head(head_coords, tail_coords):
        continue

    # move tail in intended direction, following head
    # then add tails position to tail_visited list
    else:
        # figure out if head is two away horizontally/vertically, or diagonally
        for i in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            if (tail_coords[0] + i[0], tail_coords[1] + i[1]) == head_coords:
                # move tail one forward in direction head is from itself
                tail_coords = (
                    tail_coords[0] + (i[0] // 2),
                    tail_coords[1] + (i[1] // 2),
                )
                tail_visited.append(tail_coords)
                break

        # tail needs to move diagonally
        else:
            vector: tuple[int, int] = (
                head_coords[0] - tail_coords[0],
                head_coords[1] - tail_coords[1],
            )
            if vector[0] in [-2, 2]:
                tail_offset = (vector[0] // 2, vector[1])

            # elif vector[1] in [-2, 2]:
            else:
                tail_offset = (vector[0], vector[1] // 2)
            tail_coords = (
                tail_coords[0] + tail_offset[0],
                tail_coords[1] + tail_offset[1],
            )
            tail_visited.append(tail_coords)


print(len(set(tail_visited)))
