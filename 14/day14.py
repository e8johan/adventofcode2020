import re

def a(instrs):
    mem = {}
    
    mask = 0
    value = 0
    
    for i in instrs:
        if i.startswith('mask = '):
            m = i[7:]
            value = int(m.replace('X', '0'), 2)
            mask = int(m.replace('1', '0').replace('X', '1'), 2)
        else:
            m = re.match(r"^mem\[(\d+)\] = (\d+)$", i)
            mem[int(m.group(1))] = (int(m.group(2))&mask)|value
                    
    res = 0
    for v in mem.values():
        res += v

    return res

def write(mem, mask, address, value):
    xpos = mask.find('X')
    if xpos == -1:
        mem[address|int(mask, 2)] = value
    else:
        write(mem, mask[:xpos] + "0" + mask[xpos+1:], address, value)
        write(mem, mask[:xpos] + "1" + mask[xpos+1:], address, value)

def b(instrs):
    mem = {}
    
    mask = ''
    
    for i in instrs:
        if i.startswith('mask = '):
            mask = i[7:]
        else:
            m = re.match(r"^mem\[(\d+)\] = (\d+)$", i)
            write(mem, mask, int(m.group(1))&int(mask.replace('0', '1').replace('X', '0'), 2), int(m.group(2)))
                    
    res = 0
    for v in mem.values():
        res += v

    return res

def test_a():
    assert a([
              'mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X',
              'mem[8] = 11',
              'mem[7] = 101',
              'mem[8] = 0',
          ]) == 165

def test_b():
    assert b([
              'mask = 000000000000000000000000000000X1001X',
              'mem[42] = 100',
              'mask = 00000000000000000000000000000000X0XX',
              'mem[26] = 1',
          ]) == 208

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
