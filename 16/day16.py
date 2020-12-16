import re

def parse(text):
    rules = {}
    myticket = []
    tickets = []

    state = 0
    for t in text:
        if t == '':
            state += 1
            continue
        
        if state == 0: # rules
            m = re.match(r"^(.*): (\d+)-(\d+) or (\d+)-(\d+)$", t)
            assert m
            if m:
                rules[m.group(1)] = ((int(m.group(2)), int(m.group(3))), (int(m.group(4)), int(m.group(5))))
        elif state == 1: # my ticket
            if t == 'your ticket:':
                pass
            else:
                myticket = [int(x) for x in t.split(',')]
        else: # nearby tickets
            if t == 'nearby tickets:':
                pass
            else:
                tickets.append([int(x) for x in t.split(',')])

    return rules, myticket, tickets

def a(text):
    rules, myticket, tickets = parse(text)
    
    res = 0
    for t in tickets:
        for v in t:
            found = False
            for r in rules.values():
                for s in r:
                    if v >= s[0] and v <= s[1]:
                        found = True
            if not found:
                res += v

    return res

def b_inner(text):
    rules, myticket, tickets = parse(text)
    
    # find all valid tickets
    validtickets = []
    for t in tickets:
        ticketfound = True
        for v in t:
            fieldfound = False
            for r in rules.values():
                for s in r:
                    if v >= s[0] and v <= s[1]:
                        fieldfound = True
            if not fieldfound:
                ticketfound = False
        if ticketfound:
            validtickets.append(t)
    
    # find all potential fields per position
    
    # prepare a table of all fields for all positions
    maybe = []
    for ii in range(len(myticket)):
        t = []
        for k in rules:
            t.append(k)
        maybe.append(t)
        
    # remove fields from impossible positions
    for t in validtickets:
        for ii in range(len(t)):
            v = t[ii]
            for f in rules:
                if f in maybe[ii]:
                    r = rules[f]
                    found = False
                    for s in r:
                        if v >= s[0] and v <= s[1]:
                            found = True
                    if not found:
                        maybe[ii].remove(f)
    
    # ensure that all fields are unique
    assigned = []
    while True:
        done = True
        for f in maybe:
            assert len(f) > 0
            if len(f) > 1:
                done = False
        if done:
            break
        # find first field of len 1 not in assigned
        for f in maybe:
            if len(f) == 1 and f[0] not in assigned:
                assigned.append(f[0])
                break
        # clean it out
        for f in maybe:
            if len(f) > 1:
                if assigned[-1] in f:
                    f.remove(assigned[-1])

    # build results from the unique fields
    res = {}
    for ii in range(len(maybe)):
        res[maybe[ii][0]] = myticket[ii]
    return res

def b(text):
    values = b_inner(text)
    
    res = 1
    for v in values:
        if v.startswith('departure'):
            res *= values[v]
    
    return res

def test_a():
    assert a([
        'class: 1-3 or 5-7',
        'row: 6-11 or 33-44',
        'seat: 13-40 or 45-50',
        '',
        'your ticket:',
        '7,1,14',
        '',
        'nearby tickets:',
        '7,3,47',
        '40,4,50',
        '55,2,20',
        '38,6,12',
    ]) == 71

def test_b():
    values = b_inner([
        'class: 0-1 or 4-19',
        'row: 0-5 or 8-19',
        'seat: 0-13 or 16-19',
        '',
        'your ticket:',
        '11,12,13',
        '',
        'nearby tickets:',
        '3,9,18',
        '15,1,5',
        '5,14,9',
    ])
    
    assert values['class'] == 12
    assert values['row'] == 11
    assert values['seat'] == 13

if __name__ == '__main__':
    # Input
    values = []

    # Read the input
    with open("input.txt", "r") as f:
        values = f.read().splitlines()

    print("Result a: %d" % (a(values),))
    print("Result b: %d" % (b(values),))
