with open('input.txt', 'r') as f:
    data = f.readlines()

data = data[0].split(',')
# print(data)

def simulate_day(data: list) -> list:
    '''
    Simulate 1 day.
    '''
    new_lanternfish_ages = []

    for i in data:
        i = int(i)
        if i == 0:
            new_lanternfish_ages.append(6)
            new_lanternfish_ages.append(8)

        else:
            new_lanternfish_ages.append(i - 1)

    return new_lanternfish_ages

sample_input = [2, 4, 6, 1]

for i in range(80):
    # sample_input = simulate_day(sample_input)
    data = simulate_day(data)

print(len(data))

