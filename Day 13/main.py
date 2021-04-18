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


print(problem1())
