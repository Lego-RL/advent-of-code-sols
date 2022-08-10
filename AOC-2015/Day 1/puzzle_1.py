with open("input.txt", "r") as f:
    data: str = f.read()

up: int = data.count("(")
down: int = data.count(")")

print(up - down)
