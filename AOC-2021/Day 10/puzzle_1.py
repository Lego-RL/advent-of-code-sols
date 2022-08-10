with open('input.txt', 'r') as f:
    data = f.readlines()


# with open('sample_input.txt', 'r') as f:
#     data = f.readlines()


data = [x.strip('\n') for x in data]

scores = {
    ')': 3, 
    ']': 57,
    '}': 1197,
    '>': 25137
}


open_chars = ['(', '[', '{', '<']
close_chars = [')', ']', '}', '>']

error_score = 0

for line in data:
    stack = []


    for count, char in enumerate(line):
        if char in open_chars:
            stack.append(char)

        else:
            last_opener = stack.pop()
            if open_chars.index(last_opener) != close_chars.index(char):
                error_score += scores[char]
                break


print(error_score)



