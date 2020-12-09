def find_pair(target, values):
    for ii in range(len(values)):
        for jj in range(ii+1, len(values)):
            if values[ii] + values[jj] == target:
                return True
    return False

def a(values, window=25):
    index = window
    
    while find_pair(values[index], values[index-window:index]):
        index += 1
    
    return values[index]

def b(values, window=25):
    target = a(values, window)
    
    index = 0
    offset = 0
    sum = 0
    while sum != target:
        if sum < target:
            sum += values[index+offset]
            offset += 1
        elif sum > target:
            index += 1
            offset = 0
            sum = 0
        else:
            pass # Caught by the while

    return min(values[index: index+offset]) + max(values[index:index+offset])

def test_a():
    assert a([35, 20, 15, 25, 47,
              40, 62, 55, 65, 95,
              102, 117, 150, 182, 127,
              219, 299, 277, 309, 576], window=5) == 127
    
def test_b():
    assert b([35, 20, 15, 25, 47,
              40, 62, 55, 65, 95,
              102, 117, 150, 182, 127,
              219, 299, 277, 309, 576], window=5) == 62
    
    
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
