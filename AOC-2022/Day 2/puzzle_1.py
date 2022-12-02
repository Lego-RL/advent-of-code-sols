with open("input.txt", "r") as f:
    data = f.readlines()


data = [x.strip("\n") for x in data]
# data = ["A Y", "B X", "C Z"]


SHAPE: dict = {"Rock": 1, "Paper": 2, "Scissors": 3}
OUTCOME: dict = {"Lost": 0, "Draw": 3, "Won": 6}

LEFT_ITEMS: dict = {"A": "Rock", "B": "Paper", "C": "Scissors"}
RIGHT_ITEMS: dict = {"X": "Rock", "Y": "Paper", "Z": "Scissors"}

KEY: dict = {-1: "Lost", 0: "Draw", 1: "Won"}

rock_battles = [0, -1, 1]
paper_battles = [1, 0, -1]
scissors_battles = [-1, 1, 0]

score: int = 0
for game in data:
    outcome = 0

    left, right = game.split(" ")
    print(f"left: {LEFT_ITEMS[left]}, right: {RIGHT_ITEMS[right]}")
    shape = SHAPE[RIGHT_ITEMS[right]]

    if RIGHT_ITEMS[right] == "Rock":
        outcome = rock_battles[SHAPE[LEFT_ITEMS[left]] - 1]

    elif RIGHT_ITEMS[right] == "Paper":
        outcome = paper_battles[SHAPE[LEFT_ITEMS[left]] - 1]

    else:
        outcome = scissors_battles[SHAPE[LEFT_ITEMS[left]] - 1]

    print(f"shape: {shape}, outcome: {OUTCOME[KEY[outcome]]}")

    score += shape + OUTCOME[KEY[outcome]]

print(score)
