def read_input_file():
    f = open("input_file.txt", 'r')
    lst = f.readlines()
    f.close()
    return lst


passwordList = read_input_file()

secondHalfValid = valid = 0

for password in passwordList:
    lineSplit = password.split()
    letterCount = lineSplit[2].count(lineSplit[1][0])
    minAllowed, maxAllowed = lineSplit[0].split('-')
    # first half
    if int(minAllowed) <= letterCount <= int(maxAllowed):
        valid += 1
    # second half, ps too lazy to "fix" the varia
    if bool(lineSplit[2][int(minAllowed) - 1] is lineSplit[1][0]) ^ bool(lineSplit[2][int(maxAllowed) - 1] is lineSplit[1][0]):
        secondHalfValid += 1
print("First half result: {}\nSecond Half result: {}".format(valid, secondHalfValid))
