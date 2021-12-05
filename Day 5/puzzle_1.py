with open('input.txt', 'r') as f:
    data = f.readlines()

map = [ [0] * 1000 for _ in range(1000)]


for x in data:
    left, right = x.split('->')

    left = left.strip()
    right = right.strip()

    x1, y1 = left.split(',')
    x2, y2 = right.split(',')

    x1, y1 = int(x1), int(y1)
    x2, y2 = int(x2), int(y2)

    if x1 == x2:
        if y1 < y2:
            
            for i in range(y1, y2+1):

                
                if map[x1][i] == 1:
                    map[x1][i] = 2
                
                elif map[x1][i] == 2:
                    continue
                    
                #when no other line has crossed this point yet
                else:
                    map[x1][i] = 1
        #y1 > y2
        else:
            for i in range(y2, y1+1):
                if map[x1][i] == 1:
                    map[x1][i] = 2
                
                elif map[x1][i] == 2:
                    continue
                    
                #when no other line has crossed this point yet
                else:
                    map[x1][i] = 1

    #y1 == y2
    else:
        if x1 < x2:
            for i in range(x1, x2+1):
                if map[i][y1] == 1:
                    map[i][y1] = 2

                elif map[i][y1] == 2:
                    continue

                else:
                    map[i][y1] = 1

        else:
            for i in range(x2, x1+1):
                if map[i][y1] == 1:
                    map[i][y1] = 2

                elif map[i][y1] == 2:
                    continue

                else:
                    map[i][y1] = 1


count = 0
for row in map:
    for element in row:
        if element == 2:
            count += 1

print(count)