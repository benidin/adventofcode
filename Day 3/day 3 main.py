def read_input_file():
    f = open("input_file.txt", 'r')
    lst = f.readlines()
    f.close()
    return lst


def hit_the_trees(treeMap, xrate, yrate):
    treesHit = 0
    x = xrate
    for y in range(yrate, len(treeMap), yrate):
        if treeMap[y][x % (len(treeMap[0]) - 1)] == '#':
            treesHit += 1
        x += xrate
    return treesHit


trees = read_input_file()
totalTreesHit = hit_the_trees(trees, 1, 1)
totalTreesHit *= hit_the_trees(trees, 3, 1)
totalTreesHit *= hit_the_trees(trees, 5, 1)
totalTreesHit *= hit_the_trees(trees, 7, 1)
totalTreesHit *= hit_the_trees(trees, 1, 2)

print(totalTreesHit)
