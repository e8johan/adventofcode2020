def a(steps):
    directions = ((1, 0), (0, 1), (-1, 0), (0, -1)) # east, south, west, north
    
    d = 0
    pos = (0, 0)

    for s in steps:
        i = s[0]
        v = int(s[1:])
        
        if i == 'N':
            pos = (pos[0], pos[1]-v)
        elif i == 'S':
            pos = (pos[0], pos[1]+v)
        elif i == 'E':
            pos = (pos[0]+v, pos[1])
        elif i == 'W':
            pos = (pos[0]-v, pos[1])
        elif i == 'L':
            d -= int(v/90)
            while d < 0:
                d += 4
        elif i == 'R':
            d += int(v/90)
            while d > 3:
                d -= 4
        elif i == 'F':
            pos = (pos[0]+v*directions[d][0], pos[1]+v*directions[d][1])
        else:
            assert False
    
    return abs(pos[0]) + abs(pos[1])

def b(steps):
    directions = ((1, 0), (0, 1), (-1, 0), (0, -1)) # east, south, west, north
    
    wp = (10, -1)
    pos = (0, 0)

    for s in steps:
        i = s[0]
        v = int(s[1:])
        
        if i == 'N':
            wp = (wp[0], wp[1]-v)
        elif i == 'S':
            wp = (wp[0], wp[1]+v)
        elif i == 'E':
            wp = (wp[0]+v, wp[1])
        elif i == 'W':
            wp = (wp[0]-v, wp[1])
        elif i == 'L':
            d = int(v/90)
            while d>0:
                wp = (wp[1], -wp[0])
                d -= 1
        elif i == 'R':
            d = int(v/90)
            while d>0:
                wp = (-wp[1] , wp[0] )
                d -= 1
        elif i == 'F':
            pos = (pos[0] + wp[0]*v, pos[1] + wp[1]*v)
        else:
            assert False

    return abs(pos[0]) + abs(pos[1])

def test_a():
    assert a([
            'F10',
            'N3',
            'F7',
            'R90',
            'F11',
        ]) == 25

def test_b():
    assert b([
            'F10',
            'N3',
            'F7',
            'R90',
            'F11',
        ]) == 286

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
