with open('input.txt', 'r') as f:
    data = f.readlines()

map = [ [0] * 1000 for _ in range(1000)]

for row in map:
    print(len(row))


for x in data:
    left, right = x.split('->')

    left = left.strip()
    right = right.strip()

    x1, y1 = left.split(',')
    x2, y2 = right.split(',')

    x1, y1 = int(x1), int(y1)
    x2, y2 = int(x2), int(y2)

    if x1 != x2 and y1 != y2:
        continue

    if x1 == x2:
        if y1 < y2:
            loop_over = range(y1, y2+1)

        else:
            loop_over = range(y2, y1+1)
            
        for i in loop_over:
            map[x1][i] += 1

    #y1 == y2
    else:
        if x1 < x2:
            loop_over = range(x1, x2+1)

        else:
            loop_over = range(x2, x1+1)

        for i in loop_over:
            map[i][y1] += 1


count = 0
for row in map:
    for element in row:
        if element > 1:
            count += 1

print(count)