class Cpu:
    def __init__(self, code):
        self.code = code
        self.reset()
    
    def reset(self):
        self.pc = 0
        self.acc = 0
        self.visit_count = [0]*len(self.code)
        
    def step(self):
        c = self.code[self.pc]
        self.visit_count[self.pc] += 1
        ps = c.split(" ")
        i = ps[0]
        v = int(ps[1])
        if i == 'acc':
            self.acc += v
            self.pc += 1
        elif i == 'jmp':
            self.pc += v
        elif i == 'nop':
            self.pc += 1
        else:
            assert False
        
        if self.pc < 0 or self.pc >= len(self.code):
            return False
        else:
            return True

def a(code):
    c = Cpu(code)

    while True:
        acc = c.acc
        c.step()
        
        if max(c.visit_count) > 1:
            break
        
    return acc

def b(code):
    c = Cpu(code)

    for ii in range(len(code)):
        if c.code[ii].startswith('nop'):
            c.code[ii] = 'jmp' + c.code[ii][3:]
        elif c.code[ii].startswith('jmp'):
            c.code[ii] = 'nop' + c.code[ii][3:]
        
        c.reset()
        while max(c.visit_count) < 2:
            if c.step() == False:
                return c.acc

        if c.code[ii].startswith('nop'):
            c.code[ii] = 'jmp' + c.code[ii][3:]
        elif c.code[ii].startswith('jmp'):
            c.code[ii] = 'nop' + c.code[ii][3:]

    return -1

def test_a():
    assert a([
        'nop +0',
        'acc +1',
        'jmp +4',
        'acc +3',
        'jmp -3',
        'acc -99',
        'acc +1',
        'jmp -4',
        'acc +6']) == 5

def test_b():
    assert b([
        'nop +0',
        'acc +1',
        'jmp +4',
        'acc +3',
        'jmp -3',
        'acc -99',
        'acc +1',
        'jmp -4',
        'acc +6']) == 8
    
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
