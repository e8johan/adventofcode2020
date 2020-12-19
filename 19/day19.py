def parse(values):
    res_combination_rules = {}
    res_final_rules = {}
    res_messages = []
    
    in_messages = False
    for v in values:
        if v == '':
            in_messages = True
        elif not in_messages:
            t = v.split(':')
            rule_id = int(t[0])
            if len(t[1].strip()) == 3 and t[1].strip().startswith('"') and t[1].strip().endswith('"'):
                res_final_rules[rule_id] = t[1].strip()[1]
            else:
                rss = []
                for c in t[1].strip().split('|'):
                    rs = []
                    for r in c.strip().split(' '):
                        rs.append(int(r))
                    rss.append(rs)
                res_combination_rules[rule_id] = rss
        else:
            res_messages.append(v)
            
    return (res_combination_rules, res_final_rules, res_messages)

def a_match_inner(rules, msg, crules, frules):
    # recursively match from left to right
    #
    # if failed to match, bail as early as possible, no not track how many 
    # chars that where consumed as nobody will care.

    consumed = 0
    for r in rules:
        if consumed >= len(msg):
            # the msg is too short to match
            return False, -1
        
        if r in frules:
            # simple match
            if msg[consumed] == frules[r]:
                # matched, consume 1
                consumed += 1
            else:
                return (False, -1)
        else:
            matched = False
            for sr in crules[r]:
                m, c = a_match_inner(sr, msg[consumed:], crules, frules)
                if m:
                    matched = True
                    consumed += c
                    break
            if not matched:
                return (False, -1)
    
    return (True, consumed)

def a_match(msg, crules, frules):
    m, c = a_match_inner(crules[0][0], msg, crules, frules)
    if not m or c != len(msg):
        # failed to match the entire message
        return False
    
    return True

def b_match_inner(rules, msg, crules, frules, prules):
    # this is a copy paste, but should really be a refactor

    consumed = 0

    if rules == [8, 11]:
        # super special case 8, followed by 11
        # 8: 42 | 42 8
        # 11: 42 31 | 42 11 31
        # means, a number of 42s followed by a 31, should match
        # this fails because 8 consumes all 42s, so 11 never gets matched
        # the only place 8 and 11 occurs is in rule 0, as a pair
        count42s = 0
        hit42 = True
        while hit42:
            hit42 = False
            for p in prules[42]:
                if msg[consumed:].startswith(p):
                    hit42 = True
                    count42s += 1
                    consumed += len(p)
                    break
        count31s = 0
        hit31 = True
        while hit31:
            hit31 = False
            for p in prules[31]:
                if msg[consumed:].startswith(p):
                    hit31 = True
                    count31s += 1
                    consumed += len(p)
                    break

        if count42s > 1 and count31s > 0 and count31s < count42s:
            # count42s > 1, to accomodate for 8, then 11
            return (True, consumed)
        else:
            return (False, -1)

    for r in rules:
        if consumed >= len(msg):
            # the msg is too short to match
            return False, -1
        
        if r in frules:
            # simple match
            if msg[consumed] == frules[r]:
                # matched, consume 1
                consumed += 1
            else:
                return (False, -1)
        else:
            matched = False
            for sr in crules[r]:
                m, c = a_match_inner(sr, msg[consumed:], crules, frules)
                if m:
                    matched = True
                    consumed += c
                    break
            if not matched:
                return (False, -1)
    
    return (True, consumed)

def b_match(msg, crules, frules, prules):
    m, c = b_match_inner(crules[0][0], msg, crules, frules, prules)
    if not m or c != len(msg):
        # failed to match the entire message
        return False
    
    return True

def b_create_string(rules, crules, frules):
    # recursively map out all possible combinations of a list of rules
    
    res = []
    
    for r in rules:
        if r in frules:
            if len(res) > 0:
                tres = []
                for r1 in res:
                    tres.append(r1 + frules[r])
                res = tres
            else:
                res.append(frules[r])
        else:
            if len(res) > 0:
                combine_res = True
            else:
                combine_res = False
                
            tres = []
            for sr in crules[r]:
                sres = b_create_string(sr, crules, frules)
                if combine_res:
                    for r1 in res:
                        for r2 in sres:
                            tres.append(r1+r2)
                else:
                    for r1 in sres:
                        res.append(r1)
            if combine_res:
                res = tres

    return res

def b_precalculate_rules(rules, crules, frules):
    res = {}
    for r1 in rules:
        res[r1] = []
        for r2 in crules[r1]:
            res[r1] = [*res[r1], *b_create_string(r2, crules, frules)]
    return res

def a(values):
    crules, frules, messages = parse(values)
    
    res = 0
    for m in messages:
        if a_match(m, crules, frules):
            res += 1
    
    return res

def b(values):    
    crules, frules, messages = parse(values)
    
    # overriding the rules
    crules[8] = [[42], [42, 8]]
    crules[11] = [[42, 31], [42, 11, 31]]

    # precalculating the "stop conditions" for the loops
    prules = b_precalculate_rules([31, 42], crules, frules)
    
    res = 0
    for m in messages:
        if b_match(m, crules, frules, prules):
            res += 1
    
    return res

def test_a():
    assert a([
        '0: 4 1 5',
        '1: 2 3 | 3 2',
        '2: 4 4 | 5 5',
        '3: 4 5 | 5 4',
        '4: "a"',
        '5: "b"',
        '',
        'ababbb',
        'bababa',
        'abbbab',
        'aaabbb',
        'aaaabbb',
        ]) == 2

def test_b():
    test_data = [
        '42: 9 14 | 10 1',
        '9: 14 27 | 1 26',
        '10: 23 14 | 28 1',
        '1: "a"',
        '11: 42 31',
        '5: 1 14 | 15 1',
        '19: 14 1 | 14 14',
        '12: 24 14 | 19 1',
        '16: 15 1 | 14 14',
        '31: 14 17 | 1 13',
        '6: 14 14 | 1 14',
        '2: 1 24 | 14 4',
        '0: 8 11',
        '13: 14 3 | 1 12',
        '15: 1 | 14',
        '17: 14 2 | 1 7',
        '23: 25 1 | 22 14',
        '28: 16 1',
        '4: 1 1',
        '20: 14 14 | 1 15',
        '3: 5 14 | 16 1',
        '27: 1 6 | 14 18',
        '14: "b"',
        '21: 14 1 | 1 14',
        '25: 1 1 | 1 14',
        '22: 14 14',
        '8: 42',
        '26: 14 22 | 1 20',
        '18: 15 15',
        '7: 14 5 | 1 21',
        '24: 14 1',
        '',
        'abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa',
        'bbabbbbaabaabba',
        'babbbbaabbbbbabbbbbbaabaaabaaa',
        'aaabbbbbbaaaabaababaabababbabaaabbababababaaa',
        'bbbbbbbaaaabbbbaaabbabaaa',
        'bbbababbbbaaaaaaaabbababaaababaabab',
        'ababaaaaaabaaab',
        'ababaaaaabbbaba',
        'baabbaaaabbaaaababbaababb',
        'abbbbabbbbaaaababbbbbbaaaababb',
        'aaaaabbaabaaaaababaa',
        'aaaabbaaaabbaaa',
        'aaaabbaabbaaaaaaabbbabbbaaabbaabaaa',
        'babaaabbbaaabaababbaabababaaab',
        'aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba',
        ]
    
    assert a(test_data) == 3
    assert b(test_data) == 12

if __name__ == '__main__':
    # Input
    values = []

    # Read the input
    with open("input.txt", "r") as f:
        values = f.read().splitlines()

    print("Result a: %d" % (a(values),))
    print("Result b: %d" % (b(values),))
