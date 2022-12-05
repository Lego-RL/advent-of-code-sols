with open("input.txt", "r") as f:
    data = f.readlines()


def find_first_char(line: str):
    """
    Return first appearing character
    """

    line = line.strip()
    if line != "":
        return line[0]


stacks: list = []
stack_end_index: int = 0

FIRST_CHAR: int = 1
INCREMENT: int = 4

for line in data:
    if find_first_char(line) != "1":
        stack_end_index += 1
    else:
        break


for i in range(0, (len(data[0]) // 4)):  # zero through eight
    stack = []
    for j in range(stack_end_index - 1, -1, -1):  # 7 to 0
        char_index = FIRST_CHAR + (INCREMENT * i)

        char = data[j][char_index]

        if char != " ":
            stack.append(char)

    stacks.append(stack)

# instructions half
for i in range(stack_end_index + 2, len(data)):
    instruction = data[i]

    parts = instruction.split(" ")

    # subtract since indices given are 1 based, code is 0 based
    num_move, from_stack, to_stack = int(parts[1]), int(parts[3]) - 1, int(parts[5]) - 1

    for i in range(num_move):
        stacks[to_stack].append(stacks[from_stack].pop())

code = ""
for stack in stacks:
    code += stack[-1]  # just need character on top of each stack

print(code)
