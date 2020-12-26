def a(values, rounds = 100):
    vs = []
    for v in values:
        vs.append(int(v))
        
    minimum = min(vs)
    maximum = max(vs)
    
    while rounds > 0:
        # current is always left-most
        current = vs[0]

        # extract pick
        picked = vs[1:4]
        vs = vs[0:1] + vs[4:]

        # calculate dest value
        destvalue = current - 1
        if destvalue < minimum:
            destvalue = maximum
        while destvalue in picked:
            destvalue = destvalue - 1
            if destvalue < minimum:
                destvalue = maximum
        # find dest and insert pick
        dest = vs.index(destvalue)
        vs = vs[0:dest+1] + picked + vs[dest+1:]
        
        # rotate one step to the right
        vs = vs[1:] + vs[0:1]
        
        rounds -= 1

    # find 1 and align
    one = vs.index(1)
    vs = vs[one+1:] + vs[:one]
    
    # join as string
    return ''.join([str(x) for x in vs])

class LLNode:
    def __init__(self, value, parent = None):
        self.value = value
        self.previous = parent
        if parent:
            parent.next = self
        self.next = None

def llprint(node):
    n = node
    vs = []
    while True:
        vs.append(str(n.value))
        n = n.next
        if n == node:
            break
    print(", ".join(vs))

def ab(values, rounds = 100):    
    nodeforval = {}
    prev = None
    current = None
    for v in values:
        node = LLNode(int(v), prev)
        nodeforval[int(v)] = node
        if not current:
            current = node
        prev = node
        
    minimum = 1
    maximum = 9
    
    # make the snake bite its head
    prev.next = current
    current.previous = prev
    
    pickvals = [-1, -1, -1]
    destnode = current
    
    while rounds > 0:
        currentvalue = current.value
        pickstart = current.next
        pickend = pickstart
        pickvals[0] = pickend.value
        if destnode == pickend:
            destnode = current
        pickend = pickend.next
        pickvals[1] = pickend.value
        if destnode == pickend:
            destnode = current
        pickend = pickend.next
        pickvals[2] = pickend.value
        if destnode == pickend:
            destnode = current

        # extract pick
        current.next = pickend.next
        pickend.next.previous = current
        pickstart.previous = None
        pickend.next = None
        
        # calculate dest value
        destvalue = currentvalue - 1
        if destvalue < minimum:
            destvalue = maximum
        while destvalue in pickvals:
            destvalue = destvalue - 1
            if destvalue < minimum:
                destvalue = maximum
                
        # find dest and insert pick
        destnode = nodeforval[destvalue]
        pickend.next = destnode.next
        pickstart.previous = destnode
        destnode.next.previous = pickend
        destnode.next = pickstart

        current = current.next
                
        rounds -= 1

    # find 1 and align
    while destnode.value != 1:
        destnode = destnode.next
    destnode = destnode.next
    res = ''
    while destnode.value != 1:
        res += str(destnode.value)
        destnode = destnode.next

    return res


def b(values, rounds = 10000000):    
    # I could have guessed it - of course the b exercise is a lot larger
    # We need to go circular linked list - we cannot copy data around
    
    nodeforval = {}
    prev = None
    current = None
    for v in values:
        node = LLNode(int(v), prev)
        nodeforval[int(v)] = node
        if not current:
            current = node
        prev = node
        
    minimum = 1
    maximum = 9
    
    for v in range(maximum+1, 1000001):
        node = LLNode(v, prev)
        nodeforval[int(v)] = node
        prev = node
        
    # make the snake bite its head
    prev.next = current
    current.previous = prev
    
    maximum = 1000000
        
    pickvals = [-1, -1, -1]
    destnode = current
    
    while rounds > 0:
        currentvalue = current.value
        pickstart = current.next
        pickend = pickstart
        pickvals[0] = pickend.value
        if destnode == pickend:
            destnode = current
        pickend = pickend.next
        pickvals[1] = pickend.value
        if destnode == pickend:
            destnode = current
        pickend = pickend.next
        pickvals[2] = pickend.value
        if destnode == pickend:
            destnode = current

        # extract pick
        current.next = pickend.next
        pickend.next.previous = current
        pickstart.previous = None
        pickend.next = None

        # calculate dest value
        destvalue = currentvalue - 1
        if destvalue < minimum:
            destvalue = maximum
        while destvalue in pickvals:
            destvalue = destvalue - 1
            if destvalue < minimum:
                destvalue = maximum
                
        # find dest and insert pick
        destnode = nodeforval[destvalue]
        pickend.next = destnode.next
        pickstart.previous = destnode
        destnode.next.previous = pickend
        destnode.next = pickstart

        current = current.next
                
        rounds -= 1

    # find 1 and the following two values
    one = nodeforval[1]
    k = one.next.value
    l = one.next.next.value

    return k*l

def test_a():
    assert a('389125467', rounds = 10) == '92658374'
    assert a('389125467') == '67384529'
    assert ab('389125467', rounds = 10) == '92658374'
    assert ab('389125467') == '67384529'

def test_b():
    assert b('389125467') == 149245887792

if __name__ == '__main__':
    # Input
    values = []

    # Read the input
    with open("input.txt", "r") as f:
        values = f.read().strip()

    print("Result a: %s" % (a(values),))
    print("Result b: %d" % (b(values),))
