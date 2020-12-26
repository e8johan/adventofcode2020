def loopsize(sn, target):
    v = 1
    loops = 0
    while v != target:
        v *= sn
        v = v % 20201227
        loops += 1
    
    return loops

def loopvalue(iv, loops):
    v = 1
    while loops > 0:
        v *= iv
        v = v % 20201227
        loops -= 1
        
    return v

def a(door, card):
    lsdoor = loopsize(7, door)
    lscard = loopsize(7, card)
    
    ecdoor = loopvalue(card, lsdoor)
    eccard = loopvalue(door, lscard)
    
    assert ecdoor == eccard
    
    return ecdoor

def b(door, card):    
    return -1

def test_a():
    assert loopsize(7, 5764801) == 8
    assert loopsize(7, 17807724) == 11
    assert a(5764801, 17807724) == 14897079

def test_b():
    pass

if __name__ == '__main__':
    # Input
    values = []

    # Read the input
    with open("input.txt", "r") as f:
        values = f.read().splitlines()

    print("Result a: %s" % (a(int(values[0]), int(values[1])),))
    print("Result b: %d" % (b(int(values[0]), int(values[1])),))
