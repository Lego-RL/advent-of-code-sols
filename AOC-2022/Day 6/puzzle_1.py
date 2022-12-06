with open("input.txt", "r") as f:
    data = f.readlines()


data = [x.strip("\n") for x in data]
data = data[0]


for i in range(3, len(data)):
    temp: list = []
    temp.extend([data[i - 3], data[i - 2], data[i - 1], data[i]])

    if len(set(temp)) == 4:
        print(i + 1)
        break
