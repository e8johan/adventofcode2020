def a(table):
    assert len(table) == 2
    
    target = int(table[0])
    
    busses = []
    for b in table[1].split(','):
        if b == 'x':
            pass
        else:
            busses.append(int(b))
        
    earliest = -1
    earliestbus = 0
    for b in busses:
        i = int(target / b)
        if i*b < target: 
            # Adjust once for rounding
            i += 1
        if earliest == -1 or earliest > i*b:
            earliest = i*b
            earliestbus = b

    return (earliest-target)*earliestbus

def b(table):
    
    # brute force, way too slow
    
    busses = []
    for b in table[1].split(','):
        if b == 'x':
            busses.append(-1)
        else:
            busses.append(int(b))
        
    found = False
    t = 0
    while not found:
        found = True
        for ii in range(1, len(busses)):
            if busses[ii] != -1:
                if (t+ii) % busses[ii] != 0:
                    found = False
                    break
        t += busses[0]
        
    return t - busses[0]

def test_a():
    assert a([
        '939', 
        '7,13,x,x,59,x,31,19'
        ]) == 295

def test_b():
    assert b([
            '', '7,13,x,x,59,x,31,19'
        ]) == 1068781

    assert b([
            '', '17,x,13,19'
        ]) == 3417

    assert b([
            '', '67,7,59,61'
        ]) == 754018

    assert b([
            '', '67,x,7,59,61'
        ]) == 779210

    assert b([
            '', '67,7,x,59,61'
        ]) == 1261476

    assert b([
            '', '1789,37,47,1889'
        ]) == 1202161486

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
