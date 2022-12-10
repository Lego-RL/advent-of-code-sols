# with open("fakeinput.txt", "r") as f:
with open("input.txt", "r") as f:
    data = f.readlines()


data = [x.strip("\n") for x in data]

# if final instruction is add, it will take 2 more cycles than length of instructions to complete
to_add: list[int] = []

for index, instruction in enumerate(data):
    if instruction == "noop":
        to_add.append(0)
        continue

    _, num_added = instruction.split(" ")
    to_add.append(0)
    to_add.append(int(num_added))

# starts at one
total: int = 1

# by default sprite starts in initial pos of 0, 1, 2
sprite_position: list[int] = [0, 1, 2]

# CRT: list[list[str]] = [["." for i in range(40)] for j in range(6)]
CRT: str = "." * (40 * 6)

for index, cycle in enumerate(to_add):
    # don't care about cycles after 240, no more CRT monitor space to display
    if index > 240:
        break

    new_sprite_middle = total % 40
    sprite_position = [new_sprite_middle - 1, new_sprite_middle, new_sprite_middle + 1]

    if index % 40 in sprite_position:
        CRT = CRT[:index] + "#" + CRT[index + 1 :]
    total += cycle

# print in sections of 40 to mimick CRT
for i in range(0, 201, 40):
    print(CRT[i : i + 40])
