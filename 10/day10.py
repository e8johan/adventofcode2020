def a(values):
    svs = sorted(values) # sorted values
    lastjolts = 0 # outlet rating
    diffs = [0]*3
    for v in svs:
        d = v-lastjolts
        diffs[d-1] += 1
        lastjolts = v
    diffs[2] += 1 # the last jump to the adaptor
    return diffs[0] * diffs[2]

def permutations(g):
    if g == 1:
        # 1 => 1
        return 1
    elif g == 2:
        # 11 => 2
        # 2
        return 2
    elif g == 3:
        # 111 => 4
        # 12
        # 21
        # 3
        return 4
    elif g > 3:
        # 1...
        # 2...
        # 3...
        return permutations(g-1) + permutations(g-2) + permutations(g-3)

def b(values):
    svs = sorted(values) # sorted values
    diffs = []
    lastjolts = 0
    for v in svs:
        diffs.append(v-lastjolts)
        lastjolts = v

    # Find the length of each group of ones
    in_ones = False
    no_ones = 0
    one_groups = []
    for ii in range(0, len(diffs)):
        if diffs[ii] == 1:
            if in_ones:
                no_ones += 1
            else:
                in_ones = True
                no_ones = 1
        else:
            if in_ones:
                in_ones = False
                if no_ones > 1:
                    one_groups.append(no_ones)                    
    if in_ones:
        in_ones = False
        if no_ones > 1:
            one_groups.append(no_ones)
    
    # Multiply all possible legal permutatations of groups of ones
    res = 1
    for group in one_groups:
        res *= permutations(group)
    return res

def test_a():
    assert a([16, 10, 15, 5, 1,
              11, 7, 19, 6, 12,
              4]) == 7*5
    
    assert a([28, 33, 18, 42, 31,
              14, 46, 20, 48, 47,
              24, 23, 49, 45, 19,
              38, 39, 11, 1, 32,
              25, 35, 8, 17, 7,
              9, 4, 2, 34, 10,
              3]) == 22*10

def test_b():
    assert b([16, 10, 15, 5, 1,
              11, 7, 19, 6, 12,
              4]) == 8
    
    assert b([28, 33, 18, 42, 31,
              14, 46, 20, 48, 47,
              24, 23, 49, 45, 19,
              38, 39, 11, 1, 32,
              25, 35, 8, 17, 7,
              9, 4, 2, 34, 10,
              3]) == 19208
    
if __name__ == '__main__':
    # Input
    values = []

    # Read the input
    with open("input.txt", "r") as f:
        line = "abc" # len must be more than zero on first invokation
        while len(line) > 0:
            line = f.readline()
            if len(line) > 0:
                values.append(int(line.strip()))

    print("Result a: %d" % (a(values),))
    print("Result b: %d" % (b(values),))
