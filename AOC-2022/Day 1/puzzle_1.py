with open("input.txt", "r") as f:
    data = f.readlines()


data = [x.strip("\n") for x in data]

highest_elf: int = 0

elf_calories: list = []
current_elf: list = []
for item in data:
    if item:
        current_elf.append(int(item))

    else:
        elf_calories.append(current_elf)
        current_elf = []

else:
    if current_elf:
        elf_calories.append(current_elf)

elf_calories = [sum(x) for x in elf_calories]

for i, elf in enumerate(elf_calories):
    print(i)
    if (cals := sum(elf)) > highest_elf:
        highest_elf = cals

    print(highest_elf)
