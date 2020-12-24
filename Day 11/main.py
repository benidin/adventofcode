def read_input_file():
    f = open("input_file.txt", 'r')
    lst = f.readlines()
    f.close()
    return lst


# a seat is '#'
def count_adjacent_filled_seats(seat_grid, row, col):
    count = 0
    for i in range(row - 1 if row > 0 else 0, len(seat_grid[0]) if row == len(seat_grid) - 1 else row + 2):
        for j in range(col - 1 if col > 0 else 0, len(seat_grid) if col == len(seat_grid) - 1 else col + 2):
            if i == row and j == col:
                continue
            elif seat_grid[i][j] == '#':
                count += 1
    return count


def count_first_seen_filled_seats(seat_grid, row, col):
    # add the direction here when a seat is encounter or edge of seat group is encountered
    encountered_seats = set()
    # number of filled seats encountered
    count = 0
    distance_from_seat = 1
    a_seat = {'#', 'L'}

    while len(encountered_seats) != 8:
        # we're at edge without seeing a seat
        if col + distance_from_seat >= len(seat_grid[0]):
            encountered_seats = encountered_seats.union({"NE", "E", "SE"})
        if col - distance_from_seat < 0:
            encountered_seats = encountered_seats.union({"NW", "W", "SW"})
        if row + distance_from_seat >= len(seat_grid):
            encountered_seats = encountered_seats.union({"SW", "S", "SE"})
        if row - distance_from_seat < 0:
            encountered_seats = encountered_seats.union({"NW", "N", "NE"})
        # prob can loop this but this is easy ;)
        # if else done in this order
        # 1 2 3 NW N NE
        # 4   5 W     E
        # 6 7 8 SW S SE
        # ps bounds checking is done via the ifs above.
        if "NW" not in encountered_seats and \
                seat_grid[row - distance_from_seat][col - distance_from_seat] in a_seat:
            if seat_grid[row - distance_from_seat][col - distance_from_seat] == '#':
                count += 1
            encountered_seats.add("NW")
        if "N" not in encountered_seats and \
                seat_grid[row - distance_from_seat][col] in a_seat:
            if seat_grid[row - distance_from_seat][col] == '#':
                count += 1
            encountered_seats.add("N")
        if "NE" not in encountered_seats and \
                seat_grid[row - distance_from_seat][col + distance_from_seat] in a_seat:
            if seat_grid[row - distance_from_seat][col + distance_from_seat] == '#':
                count += 1
            encountered_seats.add("NE")
        if "W" not in encountered_seats and \
                seat_grid[row][col - distance_from_seat] in a_seat:
            if seat_grid[row][col - distance_from_seat] == '#':
                count += 1
            encountered_seats.add("W")
        if "E" not in encountered_seats and \
                seat_grid[row][col + distance_from_seat] in a_seat:
            if seat_grid[row][col + distance_from_seat] == '#':
                count += 1
            encountered_seats.add("E")
        if "SW" not in encountered_seats and \
                seat_grid[row + distance_from_seat][col - distance_from_seat] in a_seat:
            if seat_grid[row + distance_from_seat][col - distance_from_seat] == '#':
                count += 1
            encountered_seats.add("SW")
        if "S" not in encountered_seats and \
                seat_grid[row + distance_from_seat][col] in a_seat:
            if seat_grid[row + distance_from_seat][col] == '#':
                count += 1
            encountered_seats.add("S")
        if "SE" not in encountered_seats and \
                seat_grid[row + distance_from_seat][col + distance_from_seat] in a_seat:
            if seat_grid[row + distance_from_seat][col + distance_from_seat] == '#':
                count += 1
            encountered_seats.add("SE")

        distance_from_seat += 1
    return count


def count_total_filled_seats(seat_grid):
    total_occupied = 0
    for i in range(len(seat_grid)):
        for j in range(len(seat_grid[0])):
            total_occupied += 1 if seat_grid[i][j] == '#' else 0
    return total_occupied


def printlist(list2):
    for i in range(len(list2)):
        for j in range(len(list2[0])):
            print("{}".format(list2[i][j]), end='')
        print('')


def optimize_seating(seat_grid, seat_counter):
    # ram is cheap right?
    post_grid = [line.copy() for line in seat_grid]
    pre_grid = [line.copy() for line in seat_grid]

    while True:
        for i in range(len(post_grid)):
            for j in range(len(post_grid[0])):
                if pre_grid[i][j] == '.':
                    continue
                adjacent = seat_counter(pre_grid, i, j)
                if pre_grid[i][j] == 'L' and adjacent == 0:
                    post_grid[i][j] = '#'
                elif pre_grid[i][j] == '#' and adjacent >= 5:
                    post_grid[i][j] = 'L'
        if pre_grid == post_grid:
            return count_total_filled_seats(post_grid)
        pre_grid = [line.copy() for line in post_grid]


seat_array = read_input_file()
# make life a little easier.
seat_array = [list(line.rstrip('\n')) for line in seat_array]

print("Part 1: {} Part 2: {}".format(optimize_seating(seat_array, count_adjacent_filled_seats, ),
                                     optimize_seating(seat_array, count_first_seen_filled_seats)))
