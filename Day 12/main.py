def read_input_file():
    f = open("input_file.txt", 'r')
    lst = f.readlines()
    f.close()
    return lst


class Boat:
    def __init__(self):
        # in degrees, 0 is N, 90 is E, etc
        self.facing = 90
        self.x = 0
        self.y = 0

    def left(self, rotation):
        self.facing = (self.facing + (360 - rotation)) % 360

    def right(self, rotation):
        self.facing = (self.facing + rotation) % 360

    # lets assume all facings are 0, 90, 180, 270
    def ahead_move(self, distance):
        if self.facing == 0:
            self.y += distance
        elif self.facing == 90:
            self.x += distance
        elif self.facing == 180:
            self.y -= distance
        else:
            self.x -= distance

    def directional_move(self, direction, amount):
        if direction == 'N':
            self.y += amount
        elif direction == 'E':
            self.x += amount
        elif direction == 'S':
            self.y -= amount
        elif direction == 'W':
            self.x -= amount
        else:
            print("Bad direction aborting", direction, amount)
            exit(-3)

    def calc_manhatten(self):
        return abs(self.x) + abs(self.y)


dir_list = read_input_file()
myboat = Boat()

for line in dir_list:
    if line[0] == 'L':
        myboat.left(int(line[1:]))
    elif line[0] == 'R':
        myboat.right(int(line[1:]))
    elif line[0] == 'F':
        myboat.ahead_move(int(line[1:]))
    else:
        myboat.directional_move(line[0], int(line[1:]))

print("Part 1:", myboat.calc_manhatten())
