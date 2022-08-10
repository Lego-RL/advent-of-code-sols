with open('input.txt', 'r') as f:
    data = f.readlines()


# with open('sample_input.txt', 'r') as f:
#     data = f.readlines()


data = [x.strip('\n') for x in data]

scores = {
    ')': 1, 
    ']': 2,
    '}': 3,
    '>': 4
}


open_chars = ['(', '[', '{', '<']
close_chars = [')', ']', '}', '>']

total_score = []

corrupted = []

#discard all corrupted entries
for line in data:
    stack = []

    for count, char in enumerate(line):
        if char in open_chars:
            stack.append(char)

        else:
            last_opener = stack.pop()
            if open_chars.index(last_opener) != close_chars.index(char):
                corrupted.append(line)
                break


without_corrupted = set(data) - set(corrupted)


#only incompletes
for line in without_corrupted:
    stack = []

    for count, char in enumerate(line):
        if char in open_chars:
                stack.append(char)
            
        else:
            last_opener = stack.pop()

    closing_chars = []
    for i in stack[::-1]:
        closing_chars.append(scores[close_chars[open_chars.index(i)]])

    line_score = 0
    for i in closing_chars:
        line_score *= 5
        line_score += i

    total_score.append(line_score)

total_score = sorted(total_score)
print(total_score[len(total_score) // 2])




