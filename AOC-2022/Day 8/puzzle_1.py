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


def count_visible(trees: list[Tree], debug=False) -> int:
    """
    Count how many trees are visible in given list.
    """

    if len(trees) == 1:
        return 0

    tree_count: int = 0  # by default edge/first tree can be seen

    last_tree: Tree = trees[0]
    tallest_tree: int = last_tree.number

    # count edges if not already counted
    if not last_tree.counted:
        tree_count += 1
        last_tree.counted = True

    for tree in trees[1:]:
        if (
            tree.number > tallest_tree
            and tree.number > last_tree.number
            and not tree.counted
        ):
            tallest_tree = tree.number
            tree_count += 1
            tree.counted = True

            last_tree = tree

        # if tree already counted then continue on without increasing counter
        elif tree.number > last_tree.number and tree.counted:
            last_tree = tree
            continue

        else:
            continue

    return tree_count


visible_count = 0

# visibility from left to right and right to left
for index, row in enumerate(treemap):

    visible_count += count_visible(row, debug=True)
    visible_count += count_visible(list(reversed(row)), debug=True)


# visibility from top to bottom and bottom to top
temp_tree_column: list[Tree] = []
for indexi, i in enumerate(range(len(treemap))):
    for indexj, j in enumerate(range(len(treemap[0]))):
        temp_tree_column.append(treemap[j][i])

    visible_count += count_visible(temp_tree_column, debug=True)
    visible_count += count_visible(list(reversed(temp_tree_column)), debug=True)
    temp_tree_column = []

tree_row_representation: list[str] = []
# for row in treemap:
#     for tree in row:
#         tree_row_representation.append("X" if tree.counted else "O")

#     print(tree_row_representation)
#     tree_row_representation = []

print(visible_count)
