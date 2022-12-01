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
sums: list = []
for i in range(3):
    most_cals: int = max(elf_calories)
    sums.append(most_cals)
    del elf_calories[elf_calories.index(most_cals)]

print(sum(sums))
