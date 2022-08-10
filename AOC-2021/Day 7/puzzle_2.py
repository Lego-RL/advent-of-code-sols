from statistics import median
from copy import deepcopy

with open('input.txt', 'r') as f:
    data = f.readlines()

data = data[0].split(',')

data = [int(x) for x in data]


def test_num(gather: int) -> int:
    fuel = 0

    for i in data:
        if i == gather:
            continue
        
        absolute = abs(i - gather)
        for i in range(absolute+1):
            fuel += i

    return fuel


min_fuel = test_num(data[0])
for i in range(min(data), max(data)):
    fuel_cost = test_num(i)

    if fuel_cost < min_fuel:
        min_fuel = fuel_cost


print(min_fuel)