def a(world):
    prev_world = world[:]

    match = False
    while not match:
        next_world = []
        for yy in range(len(world)):
            line = ''
            for xx in range(len(world[yy])):
                countTaken = 0
                countFree = 0
                for iy in range(max(0, yy-1), min(len(prev_world), yy+2)):
                    for ix in range(max(0, xx-1), min(len(prev_world[yy]), xx+2)):
                        if ix == xx and iy == yy:
                            pass
                        elif prev_world[iy][ix] == 'L':
                            countFree += 1
                        elif prev_world[iy][ix] == '#':
                            countTaken += 1
                if prev_world[yy][xx] == 'L' and countTaken == 0:
                    line += '#'
                elif prev_world[yy][xx] == '#' and countTaken > 3:
                    line += 'L'
                else:
                    line += prev_world[yy][xx]
            next_world.append(line)

        match = True
        for yy in range(len(world)):
            if next_world[yy] != prev_world[yy]:
                match = False
        prev_world = next_world
        next_world = []

    count = 0
    for yy in range(len(prev_world)):
        for xx in range(len(prev_world[yy])):
            if prev_world[yy][xx] == '#':
                count += 1
    
    return count

def b(world):
    prev_world = world[:]

    match = False
    while not match:
        next_world = []
        for yy in range(len(world)):
            line = ''
            for xx in range(len(world[yy])):
                countTaken = 0
                countFree = 0
                
                directions = ((-1, 0), (-1, -1), (0, -1 ), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))
                for d in directions:
                    pos = (xx+d[0], yy+d[1])
                    while True:
                        if pos[0] < 0 or pos[0] >= len(world[yy]) or pos[1] < 0 or pos[1] >= len(world):
                            break
                        if prev_world[pos[1]][pos[0]] == 'L':
                            countFree += 1
                            break
                        if prev_world[pos[1]][pos[0]] == '#':
                            countTaken += 1
                            break
                        pos = (pos[0]+d[0], pos[1]+d[1])

                if prev_world[yy][xx] == 'L' and countTaken == 0:
                    line += '#'
                elif prev_world[yy][xx] == '#' and countTaken > 4:
                    line += 'L'
                else:
                    line += prev_world[yy][xx]
            next_world.append(line)

        match = True
        for yy in range(len(world)):
            if next_world[yy] != prev_world[yy]:
                match = False
        prev_world = next_world
        next_world = []

    count = 0
    for yy in range(len(prev_world)):
        for xx in range(len(prev_world[yy])):
            if prev_world[yy][xx] == '#':
                count += 1
    
    return count

def test_a():
    assert a([
        'L.LL.LL.LL',
        'LLLLLLL.LL',
        'L.L.L..L..',
        'LLLL.LL.LL',
        'L.LL.LL.LL',
        'L.LLLLL.LL',
        '..L.L.....',
        'LLLLLLLLLL',
        'L.LLLLLL.L',
        'L.LLLLL.LL',
        ]) == 37

def test_b():
    assert b([
        'L.LL.LL.LL',
        'LLLLLLL.LL',
        'L.L.L..L..',
        'LLLL.LL.LL',
        'L.LL.LL.LL',
        'L.LLLLL.LL',
        '..L.L.....',
        'LLLLLLLLLL',
        'L.LLLLLL.L',
        'L.LLLLL.LL',
        ]) == 26

if __name__ == '__main__':
    # Input
    values = []

    # Read the input
    with open("input.txt", "r") as f:
        line = "abc" # len must be more than zero on first invokation
        while len(line) > 0:
            line = f.readline()
            if len(line) > 0:
                values.append(line.strip())

    print("Result a: %d" % (a(values),))
    print("Result b: %d" % (b(values),))
