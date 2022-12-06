with open("input.txt", "r") as f:
    data = f.readlines()


data = [x.strip("\n") for x in data]
data = data[0]


for i in range(14, len(data)):
    temp: list = []
    for j in range(i - 13, i + 1):
        temp.append(data[j])

    print(len(temp))

    if len(set(temp)) == 14:
        print(i + 1)
        break
