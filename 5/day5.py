def seatid(code):
    assert len(code) == 7+3
    txtrow = code[:7]
    txtrow = txtrow.replace('F', '0')
    txtrow = txtrow.replace('B', '1')
    row = int(txtrow, 2)
    
    txtcol = code[-3:]
    txtcol = txtcol.replace('R', '1')
    txtcol = txtcol.replace('L', '0')
    col = int(txtcol, 2)
    
    return row*8 + col

def a(codes):
    res = -1
    for c in codes:
        sid = seatid(c)
        if sid > res:
            res = sid
    return res

def b(codes):
    sids = []
    for c in codes:
        sids.append(seatid(c))
    missing = []
    for ii in range(max(sids)):
        if ii not in sids:
            missing.append(ii)
    # since we stop at the max number, there will be no missing seats towards
    # the back, hence our seat is the last in the list
    return missing[-1]

def test_seatid():
    assert seatid('BFFFBBFRRR') == 567
    assert seatid('FFFBBBFRRR') == 119
    assert seatid('BBFFBBFRLL') == 820

def test_a():
    assert a(['BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']) == 820

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
