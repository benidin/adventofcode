def read_input_file():
    f = open("input_file.txt", 'r')
    lst = f.readlines()
    f.close()
    return lst


def problem1():
    # we always assume our input is perfect in AoC :)
    answer = [-3, -3]
    input_ = read_input_file()
    buses = input_[1].split(',')
    earliest_time = int(input_[0])

    for item in buses:
        if not str.isnumeric(item):
            continue  # we got ourselves an 'x' or not a number

        bus_id = int(item)
        minutes = bus_id - (earliest_time % bus_id)

        if answer[0] == -3 or answer[1] > minutes:
            answer[0] = bus_id
            answer[1] = minutes

    return answer[0] * answer[1]


# note I did get a hint on the start of the number theory for this solution :/
# prime numbers are fun I learned (or probably relearned about coprimes, college was a long time ago)
def problem2():
    input_ = read_input_file()

    # fix list of busses & their times so we don't have to search forward eatch time
    i = 0
    buses = list()
    for bus in input_[1].split(','):
        if bus != 'x':
            buses.append([int(bus), i])
        i += 1
    del i, bus

    current_time = adder = buses[0][0]

    for t in range(len(buses) - 1):
        while not (current_time + buses[t + 1][1]) % buses[t + 1][0] == 0:
            current_time += adder
        adder = adder * buses[t + 1][0]

    return current_time


print(problem1())

print(problem2())
