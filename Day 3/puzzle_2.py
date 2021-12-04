from copy import deepcopy

with open('input.txt', 'r') as f:
    data = f.readlines()

data = [x.strip() for x in data] #remove newlines


def find_most_common_bit(position: int, lst: list):
    '''
    Find whether 0 or 1 is most common
    bit in given position of every binary
    number in data.
    '''

    zeroes, ones = 0, 0

    for binary in lst:
        match binary[position]:
            case '0':
                zeroes += 1

            case '1':
                ones += 1


    if zeroes == ones:
        return None

    if zeroes > ones:
        return '0'

    else:
        return '1'



# 1) take list of all binary nums
# 2) remove every binary number that doesn't have the majority bit in position x
# 3) if only 2 binary numbers left, find first digit where they differ and take the num that has bit you are searching for

position = 0
test_for = 'o2'
# test_for = 'co2'

if test_for == 'o2':
    search_for_bit = '1'

else:
    search_for_bit = '0'


while position < len(data[0]):
    majority_bit = find_most_common_bit(position, data)
    if majority_bit is None: #if equal 1s and 0s then only take out numbers that are 1 or only take out nums that are 0
        data = [x for x in data if x[position] == search_for_bit]

    else:
        match test_for:
            case 'o2':
                data = [x for x in data if x[position] == majority_bit]

            case 'co2':
                data = [x for x in data if x[position] != majority_bit]

    if len(data) == 1:
        print(data[0])
        exit(0)


    elif len(data) == 2:
        while data[0][position] == data[1][position]:
            position += 1

        if data[0][position] == search_for_bit:
            print(data[0])
            exit(0)

        elif data[1][position] == search_for_bit:
            print(data[1])
            exit(0)

    position += 1


