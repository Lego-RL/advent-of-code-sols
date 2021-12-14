from string import ascii_uppercase
from copy import deepcopy
from math import ceil

with open('input.txt', 'r') as f:
    data = f.read().splitlines()

template = data.pop(0) #first template
del data[0] #empty line

rules = {}
pairs = {}
char_counts = {}

for char in ascii_uppercase:
    char_counts[char] = 0


for rule in data: #fill in rules dictionary
    pair, insertant = rule.split(' -> ')
    rules[pair] = insertant

counts = [0] * len(rules)
index_locator_helper = list(rules.keys())

#initial counts
for i in range(len(template)-1):
    pair = f'{template[i]}{template[i+1]}'
    counts[index_locator_helper.index(pair)] += 1


def step():
    global counts
    temp_counts_copy = deepcopy(counts)
    for index, pair in enumerate(index_locator_helper):
        if counts[index] > 0:
            temp_counts_copy[index_locator_helper.index(f'{pair[0]}{rules[pair]}')] += counts[index]
            temp_counts_copy[index_locator_helper.index(f'{rules[pair]}{pair[1]}')] += counts[index]

            temp_counts_copy[index_locator_helper.index(pair)] -= counts[index]

    counts = temp_counts_copy


for i in range(40):
    step()
    
for i, pair in enumerate(index_locator_helper):
    char_counts[pair[0]] += counts[i]
    char_counts[pair[1]] += counts[i]

for key in char_counts.keys():
    char_counts[key] = ceil(char_counts[key] / 2)


print(int(max(char_counts.values()) - min([x for x in char_counts.values() if x != 0])))