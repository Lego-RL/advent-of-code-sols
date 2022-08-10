with open("input.txt", "r") as f:
    data: str = f.read()

total, index = 0, 0

for paren in data:
    index += 1

    if paren == "(":
        total += 1
    elif paren == ")":
        total -= 1

    if total == -1:
        print(index)
        break
