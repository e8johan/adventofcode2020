def print_active(world):
    
    # pretty prints a 3d world
    #
    # I left my print out points commented out in the a function
    
    minx = world[0][0]
    maxx = world[0][0]
    miny = world[0][1]
    maxy = world[0][1]
    minz = world[0][2]
    maxz = world[0][2]
    
    for a in world:
        minx = min(minx, a[0])
        maxx = max(maxx, a[0])
        miny = min(miny, a[1])
        maxy = max(maxy, a[1])
        minz = min(minz, a[2])
        maxz = max(maxz, a[2])
    
    for z in range(minz, maxz+1):
        print("z=%d" % (z))
        for y in range(miny, maxy+1):
            line = ''
            for x in range(minx, maxx+1):
                if (x,y,z) in world:
                    line += '#'
                else:
                    line += '.'
            print(line)

def count_neighbours(pos, world):
    res = 0
    
    for z in range(-1, 2):
        for y in range(-1, 2):
            for x in range(-1, 2):
                if (not (x==0 and y==0 and z==0)) and (pos[0]+x, pos[1]+y, pos[2]+z) in world:
                    res += 1
    
    return res

def a(values):
    
    # coords are (x, y, z)
    active = []
    
    y=0
    for r in values:
        x=0
        for c in r:
            if c == '#':
                active.append((x, y, 0))
            x+=1
        y+=1
    
#    print_active(active)

    rounds = 0
    while rounds < 6:
        next_active = []

        minx = active[0][0]
        maxx = active[0][0]
        miny = active[0][1]
        maxy = active[0][1]
        minz = active[0][2]
        maxz = active[0][2]

        for a in active:
            minx = min(minx, a[0])
            maxx = max(maxx, a[0])
            miny = min(miny, a[1])
            maxy = max(maxy, a[1])
            minz = min(minz, a[2])
            maxz = max(maxz, a[2])

        for z in range(minz-1, maxz+2):
            for y in range(miny-1, maxy+2):
                for x in range(minx-1, maxx+2):
                    n = count_neighbours((x, y, z), active)
                    if (x, y, z) in active:
                        # is active
                        if n == 2 or n == 3:
                            next_active.append((x, y, z))
                    else:
                        # is inactive
                        if n == 3:
                            next_active.append((x, y, z))

        active = next_active
#        print('\n\nAfter %d cycles\n' % (rounds+1))
#        print_active(active)
        
        rounds += 1
    
    return len(active)

def count_neighbours_4d(pos, world):
    res = 0
    
    for w in range(-1, 2):
        for z in range(-1, 2):
            for y in range(-1, 2):
                for x in range(-1, 2):
                    if (not (x==0 and y==0 and z==0 and w==0)) and (pos[0]+x, pos[1]+y, pos[2]+z, pos[3]+w) in world:
                        res += 1
        
    return res

def b(values):
    
    # copy pasted solution, but this really is a refactor
    #
    # currently, it takes ~2 minutes on my machine, but there is a lot of
    # reverse looking up the number of neighbours in 4d space going on, I
    # bet the count_neighbours_4d is probably the most naive way to build
    # it, so there is time to be saved. Still, star retrieved, moving on!
    
    # coords are (x, y, z, w)
    active = []
    
    y=0
    for r in values:
        x=0
        for c in r:
            if c == '#':
                active.append((x, y, 0, 0))
            x+=1
        y+=1
    
    rounds = 0
    while rounds < 6:
        next_active = []

        minx = active[0][0]
        maxx = active[0][0]
        miny = active[0][1]
        maxy = active[0][1]
        minz = active[0][2]
        maxz = active[0][2]
        minw = active[0][3]
        maxw = active[0][3]

        for a in active:
            minx = min(minx, a[0])
            maxx = max(maxx, a[0])
            miny = min(miny, a[1])
            maxy = max(maxy, a[1])
            minz = min(minz, a[2])
            maxz = max(maxz, a[2])
            minw = min(minw, a[3])
            maxw = max(maxw, a[3])

        for w in range(minw-1, maxw+2):
            for z in range(minz-1, maxz+2):
                for y in range(miny-1, maxy+2):
                    for x in range(minx-1, maxx+2):
                        n = count_neighbours_4d((x, y, z, w), active)
                        if (x, y, z, w) in active:
                            # is active
                            if n == 2 or n == 3:
                                next_active.append((x, y, z, w))
                        else:
                            # is inactive
                            if n == 3:
                                next_active.append((x, y, z, w))
        active = next_active
        rounds += 1
    
    return len(active)

def test_a():
    assert a([
        '.#.',
        '..#',
        '###',
    ]) == 112

def test_b():
    assert b([
        '.#.',
        '..#',
        '###',
    ]) == 848

if __name__ == '__main__':
    # Input
    values = []

    # Read the input
    with open("input.txt", "r") as f:
        values = f.read().splitlines()

    print("Result a: %d" % (a(values),))
    print("Result b: %d" % (b(values),))
