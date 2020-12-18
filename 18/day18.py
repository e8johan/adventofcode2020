def tokenize(expr):
    # list of tuples
    #
    #   ('N', value) => integer value
    #   ('T', char)  => token character
    res = []
    
    # Current number, might be a sequence of digits
    number = ''
    while True:
        # Current token, if found
        found_token = ''
        # True if whitespace is found
        found_whitespace = False
        
        peek = expr[0]
        if peek in '0123456789': 
            # part of number
            number += peek
        elif peek in '()+*': 
            # token
            found_token = peek
        elif peek in ' ': 
            # whitespace
            found_whitespace = True
        
        # If we have a token or whitespace, the number has ended
        if found_token != '' or found_whitespace:
            if number != '':
                res.append(('N', int(number)))
                number = ''
    
        # Append any found tokens
        if found_token != '':
            res.append(('T', found_token))
        
        # Check if we can continue
        if len(expr) > 1:
            expr = expr[1:]
        else:
            break
    
    # Append any left-over number
    if number != '':
        res.append(('N', int(number)))

    return res
        
def a_expression(tokens, ind=0):
    
    # ind is used to indent prints
    # I left the prints I used for debugging commented out below
    #
    # this solution uses a flat while loop to multiply and add, and recursion 
    # only for parenthesises
    
    res_value = 0
    res_consumed = 0
    
    if tokens[0] == ('T', '('):
        v, c = a_expression(tokens[1:], ind+2)
        res_value = v
        res_consumed = 2+c
        assert tokens[1+c] == ('T', ')')
    elif tokens[0][0] == 'N':
        res_value = tokens[0][1]
        res_consumed = 1
        #print(' '*ind + "VALUE %d" % (res_value))
        
    while True:
        #print(' '*ind + "loop %d, %d" % (res_value, res_consumed))
        if len(tokens) == res_consumed:
            #print(' '*ind + "ENDEXPR")
            break
        elif tokens[res_consumed] == ('T', ')'):
            #print(' '*ind + "ENDPAREN")
            break
        elif tokens[res_consumed] == ('T', '+'):
            #print(' '*ind + "ADD")
            res_consumed += 1
            if tokens[res_consumed][0] == 'N':
                #print(' '*ind + "NUM %d" % (tokens[res_consumed][1]))
                res_value += tokens[res_consumed][1]
                res_consumed += 1
            elif tokens[res_consumed] == ('T', '('):
                res_consumed += 1
                v, c = a_expression(tokens[res_consumed:], ind+2)
                res_value += v
                res_consumed += c
                assert tokens[res_consumed] == ('T', ')')
                res_consumed += 1
            else:
                assert False
        elif tokens[res_consumed] == ('T', '*'):
            #print(' '*ind + "MUL")
            res_consumed += 1
            if tokens[res_consumed][0] == 'N':
                #print(' '*ind + "NUM %d" % (tokens[res_consumed][1]))
                res_value *= tokens[res_consumed][1]
                res_consumed += 1
            elif tokens[res_consumed] == ('T', '('):
                res_consumed += 1
                v, c = a_expression(tokens[res_consumed:], ind+2)
                res_value *= v
                res_consumed += c
                assert tokens[res_consumed] == ('T', ')')
                res_consumed += 1
            else:
                assert False
        else:
            assert False
    else:
        assert False
        
    #print(' '*ind + "=> %d, %d" % (res_value, res_consumed))
        
    return (res_value, res_consumed)

def b_value(tokens):
    res_value = 0
    res_consumed = 0
    
    if tokens[0] == ('T', '('):
        res_consumed += 1
        
        v, c = b_mul_expression(tokens[1:])
        res_value = v
        res_consumed += c
        
        assert tokens[res_consumed] == ('T', ')')
        res_consumed += 1
    elif tokens[0][0] == 'N':
        res_value = tokens[0][1]
        res_consumed += 1
        
    return (res_value, res_consumed)

def b_mul_expression(tokens):
    res_value, res_consumed = b_add_expression(tokens)
    
    while res_consumed < len(tokens) and tokens[res_consumed] == ('T', '*'):
        res_consumed += 1

        v, c = b_add_expression(tokens[res_consumed:])
        res_value *= v
        res_consumed += c

    return (res_value, res_consumed)

def b_add_expression(tokens):
    res_value, res_consumed = b_value(tokens)
    
    while res_consumed < len(tokens) and tokens[res_consumed] == ('T', '+'):
        res_consumed += 1
        
        v, c = b_value(tokens[res_consumed:])
        res_value += v
        res_consumed += c
    
    return (res_value, res_consumed)

def b_expression(tokens):
    
    # as we have operator precedence, this solution uses recursion to encode
    # this. The outer function (this one), is more or less a wrapper, just to
    # avoid having to show that the mul is the outer evalution.
    #
    # the hierarcy is:
    #
    #   mul  <---- evaluated last
    #   add
    #   value <--- evaluated first
    #
    # the value can be either an integer, or a sub-expression, i.e. 
    # '(' + mul + ')'
    #
    # mul and add will act as a pass-through for the value if no '*' or '+'
    # operator is encountered.
    
    res_value = 0
    res_consumed = 0
    
    v, c = b_mul_expression(tokens)
    res_value += v
    res_consumed += c
    
    return (res_value, res_consumed)

def inner_a(expr):
    tokens = tokenize(expr)
    value, consumed = a_expression(tokens)
    assert consumed == len(tokens)
    return value

def a(values):
    res = 0
    for v in values:
        res += inner_a(v)
        
    return res

def inner_b(expr):
    tokens = tokenize(expr)
    value, consumed = b_expression(tokens)
    assert consumed == len(tokens)
    return value

def b(values):
    res = 0
    for v in values:
        res += inner_b(v)
        
    return res

def test_a():
    assert inner_a('1 + 2 * 3 + 4 * 5 + 6') == 71
    assert inner_a('1 + (2 * 3) + (4 * (5 + 6))') == 51
    assert inner_a('2 * 3 + (4 * 5)') == 26
    assert inner_a('5 + (8 * 3 + 9 + 3 * 4 * 3)') == 437
    assert inner_a('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))') == 12240
    assert inner_a('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == 13632

def test_b():
    assert inner_b('1 + (2 * 3) + (4 * (5 + 6))') == 51
    assert inner_b('2 * 3 + (4 * 5)') == 46
    assert inner_b('5 + (8 * 3 + 9 + 3 * 4 * 3)') == 1445
    assert inner_b('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))') == 669060
    assert inner_b('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == 23340

if __name__ == '__main__':
    # Input
    values = []

    # Read the input
    with open("input.txt", "r") as f:
        values = f.read().splitlines()

    print("Result a: %d" % (a(values),))
    print("Result b: %d" % (b(values),))
