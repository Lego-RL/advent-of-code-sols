# with open("fakeinput.txt", "r") as f:
with open("input.txt", "r") as f:
    data = f.readlines()


def compare_pairs(pair1: list | int, pair2: list | int) -> bool | None:
    """
    Return whether the pair is in the right order or not.
    """

    list1: list[int] = []
    list2: list[int] = []

    if isinstance(pair1, int) and isinstance(pair2, int):
        if pair1 > pair2:
            return False

        elif pair1 < pair2:
            return True

    elif isinstance(pair1, list) and not isinstance(pair2, list):
        list1 = pair1
        list2 = [pair2]

    elif not isinstance(pair1, list) and isinstance(pair2, list):
        list1 = [pair1]
        list2 = pair2

    else:
        list1 = pair1
        list2 = pair2

    for index, item in enumerate(list1):

        if len(list2) <= index:
            return False

        if (result := compare_pairs(item, list2[index])) is None:
            continue

        else:
            return result

    if len(list2) > len(list1):
        return True

    return None


pairs: list[list[int]] = []

for i in range(0, len(data), 3):
    if data[i][0] == "[":
        pairs.append([eval(data[i]), eval(data[i + 1])])

indices_total: int = 0
for index, pair in enumerate(pairs):
    print(f"pair {index+1}")

    first_val, second_val = pair[0], pair[1]
    result: bool | None = compare_pairs(first_val, second_val)

    # None means completed without problems, aka pair in okay order
    if result in [True, None]:
        indices_total += index + 1


print(indices_total)
