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


# start off with given divider packets
sorted_packets = []
packets = [[[2]], [[6]]]

for i in range(len(data)):
    if data[i][0] == "[":
        packets.append([eval(data[i])])

while len(packets) > 0:
    packet = packets.pop()
    if len(sorted_packets) == 0:
        sorted_packets.append(packet)

    else:
        print(f"here")
        for index, sorted_packet in enumerate(sorted_packets[:]):
            if result := compare_pairs(packet, sorted_packet):
                sorted_packets.insert(index, packet)
                break

        # packet did not fit in before any other packets, make it final element
        else:
            sorted_packets.append(packet)


divider_packets = [[[2]], [[6]]]
decoder_key: int = 1
for packet in divider_packets:
    # add one to index by 0
    index = sorted_packets.index(packet) + 1
    decoder_key *= index

print(decoder_key)
