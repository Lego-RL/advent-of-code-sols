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

cycles_till_inspect: int = 20
inspected_values: list[int] = []

for index, cycle in enumerate(to_add):
    # don't care about cycles after 220
    if index > 220:
        break

    cycles_till_inspect -= 1
    signal_strength: int = total * (index + 1)

    if cycles_till_inspect == 0:
        inspected_values.append(signal_strength)
        cycles_till_inspect = 40

    total += cycle

print(inspected_values)
print(sum(inspected_values))
