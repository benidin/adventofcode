# day one code advent basically 2 sum


def read_input_file():
    f = open("input_file.txt", 'r')
    lst = []
    for line in f:
        lst.append(int(line))
    f.close()
    return lst


numbers_list = sorted(read_input_file())
for i in range(len(numbers_list)):
    for j in range(i + 1, len(numbers_list)):
        for k in range(j + 1, len(numbers_list)):
            if numbers_list[i] + numbers_list[j] + numbers_list[k] == 2020:
                print("{}".format(numbers_list[i] * numbers_list[j] * numbers_list[k]))
                exit()  # peace
            elif numbers_list[i] + numbers_list[j] + numbers_list[k] > 2020:
                continue
