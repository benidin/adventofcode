def read_input_file():
    f = open("input_file.txt", 'r')
    lst = f.readlines()
    f.close()
    return lst


def run_part1(operation_list):
    accumulator = 0
    ops_used = set()
    instruction_pointer = 0

    while True:
        if instruction_pointer in ops_used:
            return accumulator
        operation, argument = operation_list[instruction_pointer].split()
        argument = int(argument)

        ops_used.add(instruction_pointer)
        if operation == 'jmp':
            instruction_pointer += argument
        elif operation == 'nop':
            instruction_pointer += 1
        else:
            accumulator += argument
            instruction_pointer += 1


def run_part2(operation_list):
    op_changed_pos = set()

    while True:
        accumulator = 0
        ops_used = set()
        instruction_pointer = 0
        has_ben_changed = False

        while True:
            if instruction_pointer in ops_used or instruction_pointer >= len(operation_list):
                break
            operation, argument = operation_list[instruction_pointer].split()
            argument = int(argument)

            ops_used.add(instruction_pointer)
            if instruction_pointer not in op_changed_pos and operation != 'acc' and has_ben_changed is False:
                # swap
                operation = 'jmp' if operation == 'nop' else 'nop'
                op_changed_pos.add(instruction_pointer)
                has_ben_changed = True

            if operation == 'jmp':
                instruction_pointer += argument
            elif operation == 'nop':
                instruction_pointer += 1
            else:
                accumulator += argument
                instruction_pointer += 1

        # could return in inner loop but this is more obvious imho
        if instruction_pointer >= len(operation_list):
            return accumulator


input_list = read_input_file()

print("Part1:", run_part1(input_list), "  Part2:", run_part2(input_list))
