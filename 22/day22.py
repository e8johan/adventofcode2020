def decks(values):
    res = []
    deck = []
    
    for v in values:
        if v.startswith('Player') or v == '':
            if len(deck) > 0:
                res.append(deck)
                deck = []
        else:
            deck.append(int(v))
    
    if len(deck) > 0:
        res.append(deck)
        
    return res

def a(values):
    d1, d2 = decks(values)
    
    r = 0
    while len(d1) > 0 and len(d2) > 0:
        c1 = d1[0]
        c2 = d2[0]
        
        if c1 > c2:
            d1 = d1[1:] + [c1, c2]
            d2 = d2[1:]
        else:
            d1 = d1[1:]
            d2 = d2[1:] + [c2, c1]
            
    if len(d1) > 0:
        d = d1
    else:
        d = d2
    
    res = 0
    m = 1
    while len(d):
        res += m*d.pop()
        m += 1
        
    return res

def b(values):    
    return -1

def test_a():
    assert a([
        'Player 1:',
        '9',
        '2',
        '6',
        '3',
        '1',
        '',
        'Player 2:',
        '5',
        '8',
        '4',
        '7',
        '10',
        ]) == 306

def test_b():
    pass

if __name__ == '__main__':
    # Input
    values = []

    # Read the input
    with open("input.txt", "r") as f:
        values = f.read().splitlines()

    print("Result a: %d" % (a(values),))
    print("Result b: %d" % (b(values),))
