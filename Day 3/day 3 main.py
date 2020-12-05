def read_input_file():
    f = open("input_file.txt", 'r')
    lst = f.readlines()
    f.close()
    return lst


treeMap = read_input_file()
treesHit = 0
x = 2
for y in range(1, len(treeMap) - 1):
    if treeMap[y][x % len(treeMap[0])] == '#':
        treesHit += 1
    x += 3
print(treesHit)
