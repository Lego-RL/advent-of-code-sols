from string import ascii_letters

with open('input.txt', 'r') as f:
    data = f.readlines()

count = 0
for entry in data:
    inputs, nums = entry.split(' | ')

    inputs = inputs.split(' ')
    nums = nums.split(' ')
    nums = [x.strip('\n') for x in nums]

    

    for num in nums:
        if len(num) in [2, 4, 3, 7]: #for 1, 4, 7, 8
            count += 1


print(count)