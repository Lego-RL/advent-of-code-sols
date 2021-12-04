with open('input.txt', 'r') as f:
    data = f.readlines()

x = 0
y = 0
aim = 0

for i in data:
    direction, magnitude = i.split(' ')

    magnitude = int(magnitude)

    match direction:
        case 'forward':
            x += magnitude
            y += aim * magnitude

        case 'down':
            aim += magnitude
        
        case 'up':
            aim -= magnitude

print(x * y)