def a(values):
    # Calculate sum of two
    for ii in range(len(values)):
        for jj in range(ii+1, len(values)):
            if values[ii] + values[jj] == 2020:
                return values[ii] * values[jj]
            
def b(values):
    # Calculate sum of three
    for ii in range(len(values)):
        for jj in range(ii+1, len(values)):
            for kk in range(jj+1, len(values)):
                if ii != jj and jj != kk and ii != kk:
                    if values[ii] + values[jj] + values[kk] == 2020:
                        return values[ii] * values[jj] * values[kk]

def test_a():
    assert a([1721, 979, 366, 299, 675, 1456]) == 514579
    
def test_b():
    assert b([1721, 979, 366, 299, 675, 1456]) == 241861950

if __name__ == '__main__':
    # Input
    values = []

    # Read the input
    with open("input.txt", "r") as f:
        line = "abc" # len must be more than zero on first invokation
        while len(line) > 0:
            line = f.readline()
            if len(line) > 0:
                values.append(int(line))

    print("Result a: %d" % (a(values),))
    print("Result b: %d" % (b(values),))
