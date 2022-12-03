from string import ascii_uppercase

with open("input.txt", "r") as f:
    data = f.readlines()


data = [x.strip("\n") for x in data]
# data = [
#     "vJrwpWtwJgWrhcsFMMfFFhFp",
#     "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
#     "PmmdzqPrVvPwwTWBwg",
#     "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
#     "ttgJtRGJQctTZtZT",
#     "CrZsJsPPZsGzwwsLwLmpwMDw",
# ]

sum: int = 0
for rucksack in data:
    left, right = rucksack[: len(rucksack) // 2], rucksack[len(rucksack) // 2 :]

    for char in left:
        if char in right:
            if char in ascii_uppercase:
                priority: int = ord(char) - 38

            else:
                priority: int = ord(char) - 96

            print(f"priority of {char} is {priority=}")
            sum += priority
            break


print(sum)
