with open("input.txt", "r") as f:
    data = f.read()

up, down = data.count("("), data.count(")")

print(up - down)
