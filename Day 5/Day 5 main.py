from math import ceil


def read_input_file():
    f = open("input_file.txt", 'r')
    lst = f.readlines()
    f.close()
    return lst


def decode(letterGroup, lowerCode, upperCode, lowerRange, upperRange):
    for code in letterGroup:
        movement = ceil((upperRange - lowerRange) / 2)
        if code == lowerCode:
            upperRange -= movement
        elif code == upperCode:
            lowerRange += movement
    return lowerRange


def find_seat(seatList):
    seatList.sort()
    for i in range(5, len(seatList) - 5):
        if seatList[i] + 1 != (seatList[i + 1]):
            return seatList[i] + 1


biggusPassuss = 0
boardingPasses = read_input_file()
seats = []

for bp in boardingPasses:
    row = decode(bp[:7], 'F', 'B', 0, 127)
    column = decode(bp[7:10], 'L', 'R', 0, 7)
    seatID = row * 8 + column
    biggusPassuss = seatID if seatID > biggusPassuss else biggusPassuss
    seats.append(seatID)

print("Biggest seatID: {},  your seat: {}".format(biggusPassuss, find_seat(seats)))
