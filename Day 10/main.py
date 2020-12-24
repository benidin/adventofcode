def read_input_file():
    f = open("input_file.txt", 'r')
    lst = f.readlines()
    f.close()
    return lst


def fix_list(l):
    l.append(0)
    return sorted([int(x) for x in l])


def calc_part1(adapters):
    onejdif = 0
    threejdiff = 1
    for i in range(len(adapters) - 1):
        if adapters[i] + 1 == adapters[i + 1]:
            onejdif += 1
        elif adapters[i] + 3 == adapters[i + 1]:
            threejdiff += 1
        else:
            print("this shouldn't happen")
    return onejdif * threejdiff


def calc_part2(adapters):
    # incomplete
    return "Incomplete"


adapter_list = fix_list(read_input_file())

print("Part 1:", calc_part1(adapter_list), "Part 2:", calc_part2(adapter_list))
