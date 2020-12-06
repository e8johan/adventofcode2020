def groups(data):
    res = []
    group = []
    for d in data:
        if len(d) == 0:
            if len(group):
                res.append(group)
            group = []
        else:
            group.append(d)
    if len(group):
        res.append(group)
    return res

def a(data):
    gs = groups(data)
    res = 0
    for g in gs:
        us = '' # unique string
        for s in g:
            for c in s:
                if c not in us:
                    us += c
        res += len(us)
    return res

def b(data):
    gs = groups(data)
    chars = "abcdefghijklmnopqrstuvwxyz"
    res = 0
    for g in gs:
        for c in chars:
            found = True
            for s in g:
                if c not in s:
                    found = False
            if found:
                res += 1
    return res

def test_groups():
    data = groups(['abc',
                   '',
                   'a',
                   'b',
                   'c',
                   '',
                   'ab',
                   'ac',
                   '',
                   'a',
                   'a',
                   'a',
                   'a',
                   '',
                   'b'])
    assert len(data) == 5
    assert len(data[0]) == 1
    assert len(data[1]) == 3
    assert len(data[2]) == 2
    assert len(data[3]) == 4
    assert len(data[4]) == 1

def test_a():
    assert a(['abc',
              '',
              'a',
              'b',
              'c',
              '',
              'ab',
              'ac',
              '',
              'a',
              'a',
              'a',
              'a',
              '',
              'b']) == 11

def test_a():
    assert b(['abc',
              '',
              'a',
              'b',
              'c',
              '',
              'ab',
              'ac',
              '',
              'a',
              'a',
              'a',
              'a',
              '',
              'b']) == 6
    
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
