def read_input_file():
    f = open("input_file.txt", 'r')
    lst = f.readlines()
    f.close()
    return lst


def XMAS_number_check(prev_25, number):
    for i in range(len(prev_25)):
        for j in range(i, len(prev_25)):
            if int(prev_25[i]) + int(prev_25[j]) == int(number):
                return True
    return False


def validate_XMAS(code_list):
    for i in range(25, len(code_list)):
        if not XMAS_number_check(code_list[i - 25:i], code_list[i]):
            return code_list[i]
    return -1


def find_weakness(code_list, invalid_number):
    for i in range(len(code_list)):
        sum_ = 0
        for j in range(i, len(code_list)):
            sum_ += int(code_list[j])
            if sum_ == invalid_number:
                sum_list = sorted([int(code_list[x]) for x in range(i, j)])
                return sum_list[0] + sum_list[-1]
            elif sum_ > invalid_number:
                break
    return -1


codes = read_input_file()
invalid = validate_XMAS(codes)
weakness = find_weakness(codes, int(invalid))
print("Part1: ", invalid.rstrip('\n'), "  Part2:", weakness)


