import re

def a(values):
    rules = []
    for v in values:
        m = re.match(r'^(\d+)-(\d+)\s+(\w):\s+(\w+)$', v)
        rules.append(m.groups())
        
    ok = 0
    for r in rules:
        count = 0
        for ii in range(len(r[3])):
            if r[3][ii] == r[2]:
                count += 1
        if count >= int(r[0]) and count <= int(r[1]):
            ok += 1

    return ok

def b(values):
    rules = []
    for v in values:
        m = re.match(r'^(\d+)-(\d+)\s+(\w):\s+(\w+)$', v)
        rules.append(m.groups())
        
    ok = 0
    for r in rules:
        count = 0
        if r[3][int(r[0])-1] == r[2]:
            count += 1
        if r[3][int(r[1])-1] == r[2]:
            count += 1
        if count == 1:
            ok += 1

    return ok

def test_a():
    assert a(["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]) == 2
    
def test_b():
    assert b(["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]) == 1

if __name__ == '__main__':
    # Input
    values = []

    # Read the input
    with open("input.txt", "r") as f:
        line = "abc" # len must be more than zero on first invokation
        while len(line) > 0:
            line = f.readline()
            if len(line) > 0:
                values.append(line)

    print("Result a: %d" % (a(values),))
    print("Result b: %d" % (b(values),))
