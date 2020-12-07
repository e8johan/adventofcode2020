import re

def rule(text):
    parts = text.split(' bags contain ')
    container = parts[0]
    bags = []
    for p in parts[1].split(', '):
        if p == 'no other bags.':
            pass
        else:
            m = re.match(r"^(\d+) ([a-z ]+) bags?.?$", p)
            bags.append((int(m.group(1)), m.group(2)))
    return (container, bags)

def a(bag, texts = None, rules = None, used = []):
    if texts:
        rs = []
        for t in texts:
            rs.append(rule(t))
    elif rules:
        rs = rules
    else:
        assert False
    
    res = 0
    for r in rs:
        for b in r[1]:
            if b[1] == bag:
                if r[0] not in used:
                    used.append(r[0])
                    res += 1 + a(r[0], rules = rs, used = used)
    
    return res
        
def b(bag, texts = None, rules = None):
    if texts:
        rs = []
        for t in texts:
            rs.append(rule(t))
        res = -1 # Don't count the gold bag, i.e. the first call has texts, not rules
    elif rules:
        rs = rules
        res = 0 # This is not the first level recursion, count all bags
    else:
        assert False
    
    for r in rs:
        if r[0] == bag:
            res += 1
            for bg in r[1]:
                res += bg[0] * b(bg[1], rules = rs)
    return res
    
        
def test_rule():
    assert rule('light red bags contain 1 bright white bag, 2 muted yellow bags.') == ('light red', [(1, 'bright white'), (2, 'muted yellow')])
    assert rule('dark orange bags contain 3 bright white bags, 4 muted yellow bags.') == ('dark orange', [(3, 'bright white'), (4, 'muted yellow')])
    assert rule('bright white bags contain 1 shiny gold bag.') == ('bright white', [(1, 'shiny gold')])
    assert rule('muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.') == ('muted yellow', [(2, 'shiny gold'), (9, 'faded blue')])
    assert rule('shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.') == ('shiny gold', [(1, 'dark olive'), (2, 'vibrant plum')])
    assert rule('dark olive bags contain 3 faded blue bags, 4 dotted black bags.') == ('dark olive', [(3, 'faded blue'), (4, 'dotted black')])
    assert rule('vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.') == ('vibrant plum', [(5, 'faded blue'), (6, 'dotted black')])
    assert rule('faded blue bags contain no other bags.') == ('faded blue', [])
    assert rule('dotted black bags contain no other bags.') == ('dotted black', [])

def test_a():
    assert a('shiny gold', 
             texts = ['light red bags contain 1 bright white bag, 2 muted yellow bags.', 
                      'dark orange bags contain 3 bright white bags, 4 muted yellow bags.', 
                      'bright white bags contain 1 shiny gold bag.', 
                      'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.', 
                      'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.', 
                      'dark olive bags contain 3 faded blue bags, 4 dotted black bags.', 
                      'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.', 
                      'faded blue bags contain no other bags.', 
                      'dotted black bags contain no other bags.']) == 4

def test_b():
    assert b('shiny gold', 
             texts = ['light red bags contain 1 bright white bag, 2 muted yellow bags.', 
                      'dark orange bags contain 3 bright white bags, 4 muted yellow bags.', 
                      'bright white bags contain 1 shiny gold bag.', 
                      'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.', 
                      'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.', 
                      'dark olive bags contain 3 faded blue bags, 4 dotted black bags.', 
                      'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.', 
                      'faded blue bags contain no other bags.', 
                      'dotted black bags contain no other bags.']) == 32

    assert b('shiny gold',
             texts = ['shiny gold bags contain 2 dark red bags.',
                      'dark red bags contain 2 dark orange bags.',
                      'dark orange bags contain 2 dark yellow bags.',
                      'dark yellow bags contain 2 dark green bags.',
                      'dark green bags contain 2 dark blue bags.',
                      'dark blue bags contain 2 dark violet bags.',
                      'dark violet bags contain no other bags.']) == 126
    
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

    print("Result a: %d" % (a('shiny gold', texts = values),))
    print("Result b: %d" % (b('shiny gold', texts = values),))
