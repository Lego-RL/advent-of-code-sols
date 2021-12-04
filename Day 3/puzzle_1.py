with open('input.txt', 'r') as f:
    data = f.readlines()

data = [x.strip() for x in data] #remove newlines
bit_positions = {}

#for however many positions there are in each binary num
for i in range(len(data[0])):
    bit_positions[i] = {0: 0, 1: 0}

for binary in data:
    for count, bit in enumerate(binary):

        if bit == '0':
            bit_positions[count][0] += 1

        else:
            bit_positions[count][1] += 1


gamma_rate, epsilon_rate = '0b', '0b'

for entry in bit_positions:
    num_zeros, num_ones = bit_positions[entry][0], bit_positions[entry][1]
    
    if num_zeros > num_ones:
        gamma_rate += '0'
        epsilon_rate += '1'

    else:
        gamma_rate += '1'
        epsilon_rate += '0'

print(int(gamma_rate, 2) * int(epsilon_rate, 2))
