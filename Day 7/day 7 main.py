def read_input_file():
    f = open("input_file.txt", 'r')
    lst = f.readlines()
    f.close()
    return lst


def load_dictionary(inputList):
    dict_ = dict()
    for line in inputList:
        line = line.rstrip('.\n')
        key, value = line.split("contain")
        key = key.rstrip(' ')
        dict_[key] = value
    return dict_


def is_bag_fittable(targetBag, bag, bagDict) -> int:
    foundBag = 0
    if bag == " no other bags":
        return 0
    elif bag.find(targetBag) >= 0:
        return 1
    else:
        bagList = [item.lstrip(' ') for item in bag.split(',')]
        for bag_ in bagList:
            bag_ = bag_[bag_.find(' ') + 1:] if bag_[0].isdigit() else bag_
            bag_ += '' if bag_[-1:] == 's' else 's'

            foundBag += is_bag_fittable(targetBag, bagDict[bag_], bagDict)

            if foundBag > 0:  # stop early
                return foundBag
    return foundBag


def part2(bag, bagDict) -> int:
    if bag == " no other bags":
        return 0
    count = 0
    bagList = [item.lstrip(' ') for item in bag.split(',')]

    for bag_ in bagList:
        numofThisVersion = int(bag_.split(' ')[0])
        bag_ = bag_[bag_.find(' ') + 1:] if bag_[0].isdigit() else bag_
        bag_ += '' if bag_[-1:] == 's' else 's'

        count += numofThisVersion * part2(bagDict[bag_], bagDict) + numofThisVersion

    return count


list_ = read_input_file()
bagDict = load_dictionary(list_)
bagsFitIn = 0
for bag in bagDict:
    if bag != "shiny gold bags":
        bagsFitIn += is_bag_fittable("shiny gold bag", bag, bagDict)

print("{}  {}".format(bagsFitIn, part2(bagDict["shiny gold bags"], bagDict)))
