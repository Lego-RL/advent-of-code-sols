with open("input.txt", "r") as f:
    # with open("fakeinput.txt", "r") as f:
    data = f.readlines()


data = [x.strip("\n") for x in data]


class Tree:
    def __init__(self, number: int, counted=False):
        self.number = number
        self.counted = counted

    def __str__(self):
        return f"Tree({self.number=}, {self.counted=})"


# convert data to ints
treemap: list[list[Tree]] = []
for row in data:
    temp: list[Tree] = []
    for element in row:
        temp.append(Tree(int(element)))

    treemap.append(temp)
    temp = []


def num_visible(from_tree: Tree, trees: list[Tree]):
    if len(trees) == 0:
        return 0

    count: int = 0
    for tree in trees:
        if from_tree.number > tree.number:
            count += 1

        elif from_tree.number <= tree.number:
            count += 1
            break

    return count


def get_scenic_score(tree: Tree, row: int, col: int) -> int:
    # left/right:
    left = treemap[row][0:col]
    try:
        right = treemap[row][col + 1 :]
    except IndexError:
        right = []

    # up/down:
    up: list = []
    down: list = []
    for i in range(len(treemap)):
        if i < row:
            up.append(treemap[i][col])

        elif i == row:
            continue

        else:
            down.append(treemap[i][col])

    # reverse left and down to sort list by view from tree
    left = list(reversed(left))
    up = list(reversed(up))

    count: int = 0
    views: list[list[Tree]] = [left, right, up, down]

    view_counts: list[int] = []
    for view in views:
        view_counts.append(num_visible(tree, view))

    scenic_score: int = view_counts[0]
    for count in view_counts[1:]:
        scenic_score *= count

    return scenic_score


highest_scenic_score: int = 0
scenic_score_map: list[list[int]] = []

# visibility from left to right and right to left
for indexi, row in enumerate(treemap):
    temp_scores = []
    for indexj, tree in enumerate(row):

        scenic_score: int = get_scenic_score(tree, indexi, indexj)
        temp_scores.append(scenic_score)
        if scenic_score > highest_scenic_score:
            highest_scenic_score = scenic_score

    scenic_score_map.append(temp_scores)
    temp_scores = []

# for row in scenic_score_map:
# print(row)

print(highest_scenic_score)
