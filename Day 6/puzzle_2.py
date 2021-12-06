from copy import deepcopy

with open('input.txt', 'r') as f:
    data = f.readlines()

data = data[0].split(',')
data = [int(x) for x in data]

DAYS = 256


def compute_one_fish(repro_in: int):

    fish_born_daily = [0] * DAYS
    days_left = DAYS

    days_left -= repro_in
    fish_born_daily[0] = 1

    for i in range(days_left):
        if i - 7 < 0:
            continue

        elif fish_born_daily[i-7] > 0:
            fish_born_daily[i] += fish_born_daily[i-7]

        if i - 9 < 0:
            continue
        
        elif fish_born_daily[i-9] > 0:
            fish_born_daily[i] += fish_born_daily[i-9]

    return sum(fish_born_daily) + 1


fish_count = 0
for i in data:
    fish_count += compute_one_fish(i)

print(fish_count)