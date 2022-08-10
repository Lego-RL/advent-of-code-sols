with open('input.txt', 'r') as f:
    data = f.readlines()


# with open('sample_input', 'r') as f:
#     data = f.readlines()


def decode_one(nums, out_nums):
    '''
    nums = first 10 groupings of letters given

    out_nums = last 4 given groupings of letters to decode

    "one" has len 2
    "seven" has len 3
    "four" has len 4
    "eight" has len 7
    '''
    

    lengths = [len(x) for x in nums]
    len_counts = {}
    for i in set(lengths):
        len_counts[str(i)] = lengths.count(i)


    rep_of_seven = set(nums[lengths.index(3)])
    rep_of_one = set(nums[lengths.index(2)])


    rep_of_four = set(nums[lengths.index(4)])
    rep_of_eight = set(nums[lengths.index(7)])

    char_a = rep_of_seven - rep_of_one 

    # representation of char c and char f between these values
    c_f = rep_of_one
    b_d = rep_of_four - rep_of_seven

    #len 5 nums
    len_fives = []
    for count, i in enumerate(lengths):
        if i == 5:
            len_fives.append(nums[count])

    #len 6 nums
    len_sixes = []
    for count, i in enumerate(lengths):
        if i == 6:
            len_sixes.append(nums[count])

    #figure out char g 
    for i in len_fives:
        if len(set(i) - b_d) == 3:
            rep_of_five = set(i)
            char_g = rep_of_five - b_d - char_a - c_f

    #figure out char e
    for i in len_fives:
        if len(set(i) - char_a - char_g - b_d - c_f) == 1:
            char_e = set(i) - char_a - char_g - b_d - c_f

    #figure out num 3
    for i in len_fives:
        if len(set(i) - b_d) == 4 and len(set(i) - char_e) == 5:
            rep_of_three = set(i)
    
    #figure out 2
    for i in len_fives:
        if set(i) != rep_of_three and set(i) != rep_of_five:
            rep_of_two = set(i)

    #figure out which is number 9
    for i in len_sixes:
        if len(set(i) - char_a - char_g - b_d - c_f) == 0:
            rep_of_nine = set(i)


    #figure out which is number 0
    for i in len_sixes:
        if len(set(i) - b_d) == 5:
            rep_of_zero = set(i)

    #figure out which is 6
    for i in len_sixes:
        if len(set(i) - char_e - b_d) == 3:
            rep_of_six = set(i)


    reps = [rep_of_zero, rep_of_one, rep_of_two, rep_of_three, rep_of_four, rep_of_five, rep_of_six, \
        rep_of_seven, rep_of_eight, rep_of_nine]

    reps = [sorted(x) for x in reps]

    final_nums = ''
    for num in out_nums:

        for iter_num, rep in enumerate(reps):
            if sorted(set(num)) == rep:
                final_nums += str(iter_num)

    return int(final_nums)

     

count = 0
for iter_num, entry in enumerate(data):
    inputs, nums = entry.split(' | ')

    inputs = inputs.split(' ')
    nums = nums.split(' ')
    nums = [x.strip('\n') for x in nums]


    count += decode_one(inputs, nums)

print(count)