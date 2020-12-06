def read_input_file():
    f = open("input_file.txt", 'r')
    lst = f.readlines()
    f.close()
    return lst


groupanswers = read_input_file()
answersP1 = set()
answersP2 = list()
countP1 = countP2 = groupSize = 0
groupanswers = [line.rstrip('\n') for line in groupanswers]

for line in groupanswers:
    if line == '':
        for item in answersP1:
            countP2 += 1 if groupSize == answersP2.count(item) else 0
        countP1 += len(answersP1)
        # reset
        groupSize = 0
        answersP2.clear()
        answersP1.clear()
    else:
        groupSize += 1
        for char in line:
            answersP1.add(char)  # cheats
            answersP2.append(char)

print("Part1: {}, Part2: {}".format(countP1, countP2))
