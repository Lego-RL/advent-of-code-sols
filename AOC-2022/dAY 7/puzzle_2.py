# with open("fakeinput.txt", "r") as f:
with open("input.txt", "r") as f:
    data = f.readlines()


data = [x.strip("\n") for x in data]


class Node:
    def __init__(self, name, parent, size=0):
        self.name = name
        self.parent = parent
        self.size = size

        self.descendants = []

    def __str__(self) -> str:
        return f"{self.name=}, {self.size=}"


root: Node = Node("/", None)
current_node: Node = root


def add_node_if_not_exist(
    current_node: Node, file_name: str, size: int = 0
) -> tuple[bool, Node]:
    """
    Returns tuple of (Bool, Node). Bool representing whether a new node was
    created or not, Node representing the desired node.
    """

    for child in current_node.descendants:
        if child.name == file_name:
            return (False, child)

    else:
        new_dir = Node(file_name, current_node, size)
        current_node.descendants.append(new_dir)
        return (True, new_dir)


index = -1  # loop starts off by adding one, starting at index 0
while index + 1 < len(data):
    index += 1

    line: str = data[index]
    if line.startswith("$"):
        new_instruct = line.strip("$").strip().split()
        # print(f"{new_instruct=}")

        match line.strip("$").strip().split():

            case ["cd", "/"]:
                continue

            case ["cd", ".."]:
                if current_node.parent:
                    current_node = current_node.parent

            case ["cd", filename]:
                response: tuple[bool, Node] = add_node_if_not_exist(
                    current_node, filename
                )
                current_node = response[1]

            # add unknown folders and add unknown files & their sizes
            case ["ls"]:
                temp_indice: int = index + 1

                # while haven't hit another instruction
                while not (result_line := data[temp_indice]).startswith("$"):
                    match result_line.split():
                        case ["dir", dirname]:  # folder
                            add_node_if_not_exist(current_node, dirname)

                        case [file_size, filename]:  # file
                            response: tuple[bool, Node] = add_node_if_not_exist(
                                current_node, filename, int(file_size)
                            )
                            if response[0] is False:  # need to update node size
                                response[1].size += int(file_size)

                    temp_indice += 1
                    if temp_indice >= len(data):
                        break
                    index += 1


def update_sizes(root):
    """
    Recursively run to the bottom of each tree and updates all
    folder sizes.
    """

    total_size: int = 0

    for child in root.descendants:
        if child.descendants:
            update_sizes(child)
        total_size += child.size

    root.size = total_size


def find_sub_goal(root: Node) -> int:
    total_sizes: int = 0

    for child in root.descendants:

        # skip files
        if not child.descendants:
            continue

        # print(child)

        if child.size < 100000:
            total_sizes += child.size + find_sub_goal(child)
            # return child.size + find_sub_goal(child)

        # file is >= 100.000 so don't consider in final num
        else:
            total_sizes += find_sub_goal(child)

    return total_sizes


def find_folder_to_del(
    root,
    TOTAL_FREE,
    delete_possibilities: list = [],
):

    for child in root.descendants:

        if not child.descendants:
            continue

        if TOTAL_FREE + child.size >= 30000000:
            delete_possibilities.append(child)

        find_folder_to_del(
            child,
            TOTAL_FREE,
            delete_possibilities,
        )

    # find smallest size in delete possibilities
    min_size: int = root.size
    for possibility in delete_possibilities:
        if possibility.size < min_size:
            min_size = possibility.size

    return min_size


def print_file_tree(root, level=0):
    print(" " * level * 2, root)

    for child in root.descendants:
        print_file_tree(child, level + 1)


def main():
    update_sizes(root)
    # print(find_sub_goal(root))

    TOTAL_FREE = 70000000 - root.size
    # print(TOTAL_FREE)
    print(find_folder_to_del(root, TOTAL_FREE))


main()
