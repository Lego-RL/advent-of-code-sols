with open('input.txt', 'r') as f:
    data = f.readlines()

x = 0
y = 0

for i in data:
    direction, magnitude = i.split(' ')

    magnitude = int(magnitude)

    match direction:
        case 'forward':
            x += magnitude

        case 'down':
            y += magnitude
        
        case 'up':
            y -= magnitude

print(x * y)