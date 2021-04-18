def read_input_file():
    f = open("input_file.txt", 'r')
    lst = f.readlines()
    f.close()
    return lst


def apply_mask(mask: str, value: int) -> int:
    for index, bit_mask in enumerate(mask):
        if bit_mask == '1':
            # "set" the bit
            value = value | (1 << (35 - index))
        elif bit_mask == '0':
            # unset the bit
            value = value & ~(1 << (35 - index))
    return value


def problem1(command_list):
    memory = dict()
    answer = 0

    for line in command_list:
        cmd, value = line.split(" = ")  # gotta love perfect input
        if cmd[:3] == 'mas':
            mask = value
        else:  # we assume we got a memory setting :)
            location = cmd.split('[')[1].split(']')[0]
            memory[location] = apply_mask(mask, int(value))

    for x in memory.values():
        answer += x

    return answer


cmds = read_input_file()
print(problem1(cmds))
