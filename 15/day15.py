def a(text):
    ns = []
    for t in text.split(","):
        ns.append(int(t.strip()))
    
    while len(ns) < 2020:
        last = ns[-1]
        index = -1
        while True:
            try:
                i = ns.index(last, index+1, len(ns)-1)
            except ValueError:
                break
            index = i
        if index == -1:
            ns.append(0)
        else:
            ns.append(len(ns)-index-1)
    
    return ns[-1]

def b(text, rounds=30000000):
    last = 0
    lastspoken = {}
    ii = 0
    
    ts = text.split(",")
    
    for t in ts[:-1]:
        last = int(t.strip())
        lastspoken[last] = ii
        ii += 1
    
    last = int(ts[-1].strip())

    while ii < rounds-1:
        if last in lastspoken:
            index = lastspoken[last]
            lastspoken[last] = ii
            last = ii-index
        else:
            lastspoken[last] = ii
            last = 0
        ii += 1
    
    return last

def test_a():
    assert a("0,3,6") == 436
    assert a("1, 3, 2") == 1
    assert a("2, 1, 3") == 10
    assert a("1, 2, 3") == 27
    assert a("2, 3, 1") == 78
    assert a("3, 2, 1") == 438
    assert a("3, 1, 2") == 1836

def test_b():
    assert b("0,3,6", 2020) == 436
    assert b("1, 3, 2", 2020) == 1
    assert b("2, 1, 3", 2020) == 10
    assert b("1, 2, 3", 2020) == 27
    assert b("2, 3, 1", 2020) == 78
    assert b("3, 2, 1", 2020) == 438
    assert b("3, 1, 2", 2020) == 1836
    assert b("0,3,6") == 175594
    assert b("1, 3, 2") == 2578
    assert b("2, 1, 3") == 3544142
    assert b("1, 2, 3") == 261214
    assert b("2, 3, 1") == 6895259
    assert b("3, 2, 1") == 18
    assert b("3, 1, 2") == 362

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

    print("Result a: %d" % (a(values[0]),))
    print("Result b: %d" % (b(values[0]),))
