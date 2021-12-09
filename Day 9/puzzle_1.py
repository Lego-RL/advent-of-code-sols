

with open('input.txt', 'r') as f:
    data = f.readlines()


data = [x.strip('\n') for x in data]

# print(data)


low_points = []

for row, i in enumerate(data):
    for col, num in enumerate(i):
        up, down = -1, -1
        left, right = -1, -1

        #no up
        if row == 0:
            #no left
            if col == 0:
                
                right = int(data[row][col+1])
                down = int(data[row+1][col])

            #there is a left
            elif col < len(data) - 1:

                left = int(data[row][col-1])
                right = int(data[row][col+1])
                down = int(data[row+1][col])

            #last col, no right
            else:
                left = int(data[row][col-1])
                down = int(data[row+1][col])



        #there is an up
        elif row < len(data[0])-1:
            #no left
            if col == 0:
                
                right = int(data[row][col+1])
                down = int(data[row+1][col])

                up = int(data[row-1][col])

            #there is a left
            elif col < len(data) - 1:

                left = int(data[row][col-1])
                right = int(data[row][col+1])
                down = int(data[row+1][col])

                up = int(data[row-1][col])

            #last col, no right
            else:
                left = int(data[row][col-1])
                down = int(data[row+1][col])
                up = int(data[row-1][col])

        #no down
        else:

            #no left
            if col == 0:
                
                right = int(data[row][col+1])

                up = int(data[row-1][col])

            #there is a left
            elif col < len(data) - 1:

                left = int(data[row][col-1])
                right = int(data[row][col+1])

                up = int(data[row-1][col])

            #last col, no right
            else:
                left = int(data[row][col-1])
                up = int(data[row-1][col])

        dirs = [up, down, left, right]
        dirs = [x for x in dirs if x != -1]

        if min(dirs) > int(num):
            low_points.append(int(num))



print(sum(low_points) + len(low_points))


