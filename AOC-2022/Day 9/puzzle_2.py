with open("input.txt", "r") as f:
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

knot_coords: list[tuple[int, int]] = []
for i in range(10):
    knot_coords.append((0, 0))

for instruction in data:
    direction, units = instruction.split(" ")
    for i in range(int(units)):
        directions.append((OFFSETS[direction]))

for direction in directions:
    offset = (int(direction[0]), int(direction[1]))
    head: tuple[int, int] = knot_coords[0]
    # prev knot starts out as head
    prev_knot_coords = (head[0] + offset[0], head[1] + offset[1])
    knot_coords[0] = (prev_knot_coords[0], prev_knot_coords[1])

    for index, knot in enumerate(knot_coords[1:]):
        # 10 tails, indices 0-9, this loop starting 1 knot after head so knot indices of 0-8 inclusive
        is_tail: bool = True if index == 8 else False

        if is_tail_adj_head(prev_knot_coords, knot):
            prev_knot_coords = knot
            continue

        # move tail in intended direction, following head
        # then add tails position to tail_visited list
        else:
            # figure out if head is two away horizontally/vertically, or diagonally
            for i in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
                if (knot[0] + i[0], knot[1] + i[1]) == prev_knot_coords:
                    # move knot one forward in direction the previous knot is from itself
                    knot_coords[index + 1] = (
                        knot_coords[index + 1][0] + (i[0] // 2),
                        knot_coords[index + 1][1] + (i[1] // 2),
                    )
                    if is_tail:
                        tail_visited.append(knot_coords[index + 1])
                    break

            # tail needs to move diagonally
            else:
                vector: tuple[int, int] = (
                    prev_knot_coords[0] - knot[0],
                    prev_knot_coords[1] - knot[1],
                )
                # if 2 off in x direction, remove magnitude and move in same direction
                tail_offset: tuple[int, int] = (
                    vector[0] // abs(vector[0]),
                    vector[1] // abs(vector[1]),
                )

                # update position of this knot
                knot_coords[index + 1] = (
                    knot_coords[index + 1][0] + tail_offset[0],
                    knot_coords[index + 1][1] + tail_offset[1],
                )
                if is_tail:
                    tail_visited.append(knot_coords[index + 1])

        prev_knot_coords = (knot_coords[index + 1][0], knot_coords[index + 1][1])

print(tail_visited)
print(len(set(tail_visited)))
