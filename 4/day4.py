import re

def read_passports(data):
    res = []
    passport = {}
    for d in data:
        if len(d) == 0:
            # Empty line, time for a new passport
            if len(passport) > 0:
                res.append(passport)
            passport = {}
        else:
            elements = d.split(' ')
            for e in elements:
                t = e.split(':')
                assert len(t) == 2
                key = t[0]
                value = t[1]
                passport[key] = value
                
    if len(passport) > 0:
        res.append(passport)

    return res
            

def a(data):
    pps = read_passports(data)
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    
    count = 0
    for pp in pps:
        valid = True
        for f in required_fields:
            if not f in pp:
                valid = False
        if valid:
            count += 1
            
    return count

def b(data):
    pps = read_passports(data)
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    allowed_fields = [*required_fields, 'cid']
    
    count = 0
    for pp in pps:
        valid = True
        for f in required_fields:
            if f in pp:
                if f == 'byr':
                    m = re.match(r"^(\d{4})$", pp[f])
                    if m:
                        v = int(m.group(1))
                        if v < 1920 or v > 2002:
                            valid = False
                    else:
                        valid = False
                elif f == 'iyr':
                    m = re.match(r"^(\d{4})$", pp[f])
                    if m:
                        v = int(m.group(1))
                        if v < 2010 or v > 2020:
                            valid = False
                    else:
                        valid = False
                elif f == 'eyr':
                    m = re.match(r"^(\d{4})$", pp[f])
                    if m:
                        v = int(m.group(1))
                        if v < 2020 or v > 2030:
                            valid = False
                    else:
                        valid = False
                elif f == 'hgt':
                    m = re.match(r"^(\d+)(in|cm)$", pp[f])
                    if m:
                        v = int(m.group(1))
                        if m.group(2) == 'cm':
                            if v < 150 or v > 193:
                                valid = False
                        else:
                            if v < 59 or v > 76:
                                valid = False
                    else:
                        valid = False
                elif f == 'hcl':
                    m = re.match(r"^#[0-9a-f]{6}$", pp[f])
                    if not m:
                        valid = False
                elif f == 'ecl':
                    m = re.match(r"^(amb|blu|brn|gry|grn|hzl|oth)$", pp[f])
                    if not m:
                        valid = False
                elif f == 'pid':
                    m = re.match(r"^(\d{9})$", pp[f])
                    if not m:
                        valid = False
            if not f in pp:
                valid = False
        else:
            if not f in allowed_fields:
                valid = False

        if valid:
            count += 1
            
    return count

def test_a():
    assert a([
        'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd',
        'byr:1937 iyr:2017 cid:147 hgt:183cm',
        '',
        'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884',
        'hcl:#cfa07d byr:1929',
        '',
        'hcl:#ae17e1 iyr:2013',
        'eyr:2024',
        'ecl:brn pid:760753108 byr:1931',
        'hgt:179cm',
        '',
        'hcl:#cfa07d eyr:2025 pid:166559648',
        'iyr:2011 ecl:brn hgt:59in',
        ]) == 2

def test_b():
    assert b([
        'pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980',
        'hcl:#623a2f',
        '',
        'eyr:2029 ecl:blu cid:129 byr:1989',
        'iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm',
        '',
        'hcl:#888785',
        'hgt:164cm byr:2001 iyr:2015 cid:88',
        'pid:545766238 ecl:hzl',
        'eyr:2022',
        '',
        'iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719',
        '',    
        'eyr:1972 cid:100',
        'hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926',
        '',
        'iyr:2019',
        'hcl:#602927 eyr:1967 hgt:170cm',
        'ecl:grn pid:012533040 byr:1946',
        '',
        'hcl:dab227 iyr:2012',
        'ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277',
        '',
        'hgt:59cm ecl:zzz',
        'eyr:2038 hcl:74454a iyr:2023',
        'pid:3556412378 byr:2007',
        '',
        ]) == 4
        
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
