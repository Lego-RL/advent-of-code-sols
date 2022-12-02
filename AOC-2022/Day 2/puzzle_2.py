with open("input.txt", "r") as f:
    data = f.readlines()


data = [x.strip("\n") for x in data]
# data = ["A Y", "B X", "C Z"]


SHAPE: dict = {"Rock": 1, "Paper": 2, "Scissors": 3}
REVERSE_SHAPE: dict = {
    1: "Rock",
    2: "Paper",
    3: "Scissors",
}  # THIS IS THE WORST CODE I HAVE EVER WRITTEN
OUTCOME: dict = {"Lost": -1, "Draw": 0, "Won": 1}

LEFT_ITEMS: dict = {"A": "Rock", "B": "Paper", "C": "Scissors"}
RIGHT_ITEMS: dict = {"X": "Lost", "Y": "Draw", "Z": "Won"}

KEY: dict = {-1: "Lost", 0: "Draw", 1: "Won"}

rock_battles = [0, -1, 1]
paper_battles = [1, 0, -1]
scissors_battles = [-1, 1, 0]
combined_battles = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]

score: int = 0
for game in data:
    outcome = 0
    shape = 0

    left, right = game.split(" ")

    goal: int = OUTCOME[RIGHT_ITEMS[right]]
    opponent: str = LEFT_ITEMS[left]
    opponent_piece_num: int = SHAPE[opponent] - 1

    for i, battle in enumerate(combined_battles):
        if battle[opponent_piece_num] == goal:
            shape = i + 1

    match right:
        case "X":
            outcome = 0
        case "Y":
            outcome = 3
        case "Z":
            outcome = 6

    score += shape + outcome

    print(f"{shape=}, {outcome=}")

print(score)
