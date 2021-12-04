previous = None
count = 0
cursor = 0
windows = []


with open('input.txt', 'r') as f:
    data = f.readlines()
    data = [int(i) for i in data]

while cursor+2 != len(data):
    windows.append(sum(data[cursor:cursor+3]))
    cursor += 1

previous = windows[0]
for i in windows[1:]:
    if i > previous:
        count += 1

    previous = i


print(count)