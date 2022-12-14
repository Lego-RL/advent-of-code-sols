with open("input.txt", "r") as f:
    # with open("fakeinput.txt", "r") as f:
    data = f.readlines()


data = [x.strip("\n") for x in data]


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x=}, {self.y=}"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash(self.__repr__())


def can_sand_move(
    rock_lines: list[Point], sand_points: list[Point], sand: Point
) -> Point | None:
    """
    If sand can move, return next point it should move to. Otherwise,
    return None if no more moves.
    """

    directly_below: Point = Point(sand.x, sand.y + 1)
    diagonal_left: Point = Point(sand.x - 1, sand.y + 1)
    diagonal_right: Point = Point(sand.x + 1, sand.y + 1)

    if directly_below not in rock_lines and directly_below not in sand_points:
        return directly_below

    elif diagonal_left not in rock_lines and diagonal_left not in sand_points:
        return diagonal_left

    elif diagonal_right not in rock_lines and diagonal_right not in sand_points:
        return diagonal_right

    else:
        return None  # unable to move


def drop_sand(rock_lines: list[Point], sand_points: list[Point], deepest_y: int):
    """
    Return sand point if it was able to successfully stop, otherwise
    None if it would endlessly fall.
    """

    sand: Point = Point(500, 0)

    while next_point := can_sand_move(rock_lines, sand_points, sand):
        if next_point.y > deepest_y:
            return None

        else:
            sand.x = next_point.x
            sand.y = next_point.y

    return sand


rock_lines: list[Point] = []
sand_points: list[Point] = []
deepest_y: int = 0


# populate rock lines
for line in data:
    coord_list: list = line.split("->")
    coord_list = [num.strip() for num in coord_list]

    points: list[Point] = []

    for coord in coord_list:
        x, y = coord.split(",")
        x, y = int(x), int(y)
        points.append(Point(x, y))

    for i in range(1, len(points)):
        first_point, second_point = points[i - 1], points[i]

        if first_point.x == second_point.x:
            if first_point.y > second_point.y:
                # swap for proper for loop range
                first_point, second_point = second_point, first_point

            for j in range(first_point.y, second_point.y + 1):
                new_point: Point = Point(first_point.x, j)
                if new_point not in rock_lines:
                    rock_lines.append(new_point)

                    # check if deepest y
                    if new_point.y > deepest_y:
                        deepest_y = new_point.y

        # the y's must be equal so only x changes
        else:
            if first_point.x > second_point.x:
                first_point, second_point = second_point, first_point

            for j in range(first_point.x, second_point.x + 1):
                new_point: Point = Point(j, first_point.y)
                if new_point not in rock_lines:
                    rock_lines.append(new_point)

num_sand_at_rest: int = 0
while new_sand := drop_sand(rock_lines, sand_points, deepest_y):
    sand_points.append(new_sand)
    num_sand_at_rest += 1

print(num_sand_at_rest)
