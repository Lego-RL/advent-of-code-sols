from collections import Counter

with open('input.txt', 'r') as f:
    data = f.read().splitlines()

template = data.pop(0)
del data[0]
rules = {}

def step(template):

    inserts = []
    
    for i in range(len(template)-1):
        pair = f'{template[i]}{template[i+1]}'
        inserts.append(rules[pair])


    rtn_template = ''
    for count, i in enumerate(template):
        rtn_template += i
        if len(inserts) > 0:
            rtn_template += inserts.pop(0)
        

    return rtn_template



for rule in data:
    pair, insertant = rule.split(' -> ')
    rules[pair] = insertant

for i in range(10):
    template = step(template)

count = Counter(template)

most_common, least_common = max(count, key=count.get), min(count, key=count.get) 
print(template.count(most_common) - template.count(least_common))