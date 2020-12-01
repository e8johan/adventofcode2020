# Input
values = []

# Read the input
with open("input.txt", "r") as f:
    line = "abc" # len must be more than zero on first invokation
    while len(line) > 0:
        line = f.readline()
        if len(line) > 0:
            values.append(int(line))

# Calculate sum of two
for ii in range(len(values)):
    for jj in range(ii+1, len(values)):
        if values[ii] + values[jj] == 2020:
            print("Result a: %d" % (values[ii] * values[jj],))
            
# Calculate sum of three
for ii in range(len(values)):
    for jj in range(ii+1, len(values)):
        for kk in range(jj+1, len(values)):
            if ii != jj and jj != kk and ii != kk:
                if values[ii] + values[jj] + values[kk] == 2020:
                    print("Result b: %d" % (values[ii] * values[jj] * values[kk],))
