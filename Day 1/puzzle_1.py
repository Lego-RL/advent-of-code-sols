previous = None
count = 0

with open('input.txt', 'r') as f:
    data = f.readlines()
    data = [int(i) for i in data]

    previous = data[0]

    for i in data[1:]:
        if i > previous:
            print(f'{i} greater than {previous}')
            count += 1
            
        previous = i

print(count)