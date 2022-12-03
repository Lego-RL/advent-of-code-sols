from string import ascii_uppercase

with open("input.txt", "r") as f:
    data = f.readlines()


data = [x.strip("\n") for x in data]

sum: int = 0
for i in range(0, len(data), 3):
    elf1, elf2, elf3 = data[i], data[i + 1], data[i + 2]

    sets = [set(elf1), set(elf2), set(elf3)]

    intersection_in_prog = sets[0].intersection(sets[1])
    final_intersection = intersection_in_prog.intersection(sets[2])

    char = list(final_intersection)[0]

    if char in ascii_uppercase:
        priority: int = ord(char) - 38

    else:
        priority: int = ord(char) - 96

    sum += priority

print(sum)
