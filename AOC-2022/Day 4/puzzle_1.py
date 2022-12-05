import time

t0 = time.time()

with open("input.txt", "r") as f:
    data = f.readlines()


data = [x.strip("\n") for x in data]

total: int = 0

for line in data:
    left, right = line.split(",")

    left_min, left_max = left.split("-")
    left_min, left_max = int(left_min), int(left_max)

    right_min, right_max = right.split("-")
    right_min, right_max = int(right_min), int(right_max)

    left_set = set(range(left_min, left_max + 1))
    right_set = set(range(right_min, right_max + 1))

    if len(left_set.intersection(right_set)) != 0:
        total += 1
        continue

print(total)
