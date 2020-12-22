def edgeint(edge):
    return int(edge.replace('.', '0').replace('#', '1'), 2)

def create_tile(tileno, tiledata):
    edge_top = edgeint(tiledata[0])
    edge_bottom = edgeint(tiledata[-1])
    
    data_left = ''
    data_right = ''
    for d in tiledata:
        data_left += d[0]
        data_right += d[-1]
    edge_left = edgeint(data_left)
    edge_right = edgeint(data_right)
    
    edge_f_top = edgeint(tiledata[0][::-1])
    edge_f_bottom = edgeint(tiledata[-1][::-1])
    edge_f_left = edgeint(data_left[::-1])
    edge_f_right = edgeint(data_right[::-1])
    
    return (tileno, [[edge_top, edge_bottom, edge_left, edge_right], 
                     [edge_f_top, edge_f_bottom, edge_left, edge_right], 
                     [edge_top, edge_bottom, edge_f_left, edge_f_right], 
                     [edge_f_top, edge_f_bottom, edge_f_left, edge_f_right]], tiledata)
    

def parse(values):
    # a tile is a (no, [[edges], [edges hflipped], [edges vflipped], [edges double flipped]], [raw tile data])
    tiles = []
    
    tileno = -1
    tiledata = []
    for v in values:
        if v.startswith('Tile '):
            if tileno > -1:
                tiles.append(create_tile(tileno, tiledata))
            
            tileno = int(v[5:-1])
            tiledata = []
        elif v == '':
            pass # just skip empty lines
        else:
            tiledata.append(v)
    if tileno > -1:
        tiles.append(create_tile(tileno, tiledata))
    
    return tiles

def check_fit(orientations, tiles):
    hits = []
    hit2 = 0
    hit3 = 0
    hit4 = 0
    for ii in range(len(orientations)):
        count = 0
        for e in tiles[ii][1][orientations[ii]]:
            for jj in range(len(orientations)):
                if ii != jj: # don't match to yourself
                    if e in tiles[jj][1][orientations[jj]]:
                        count += 1
        if count < 2 or count > 4:
            return False, []
        elif count == 2:
            hit2 += 1
            if hit2 > 4:
                return False, []
        elif count == 3:
            hit3 += 1
        elif count == 4:
            hit4 += 1
        else:
            assert False
        hits.append(count)
    
    if hit2 == 4 and \
            hit3 % 2 == 0 and hit3 > 2 and \
            hit4 == len(tiles)-4-hit3:
        return True, hits
    else:
        return False, []
    

def recursive_fit(orientations, tiles):
    # way too slow
    
    if len(orientations) < len(tiles):
        for o in range(4):
            os, hs = recursive_fit([*orientations, o], tiles)
            if len(os):
                return os, hs
        return ([], [])
    else:
        hit, hits = check_fit(orientations, tiles)
        if hit:
            return (orientations, hits)
        else:
            return ([], [])
        
def linear_fit(tiles):
    os = [0]*len(tiles)
    
    while True:
        for ii in range(len(tiles)):
            if os[ii] < 3:
                os[ii] += 1
                for jj in range(ii):
                    os[jj] = 0
                break
        else:
            break
        
        hit, hits = check_fit(os, tiles)
        if hit:
            return (os, hits)
        
    return ([], [])

def a(values):
    tiles = parse(values)
    
    res = 1
#    os, hs = recursive_fit([], tiles)
    os, hs = linear_fit(tiles)
    for ii in range(len(tiles)):
        if hs[ii] == 2:
            res *= tiles[ii][0]
    
    return res

def b(values):    
    return -1

def test_a():
    assert a([
        'Tile 2311:',
        '..##.#..#.',
        '##..#.....',
        '#...##..#.',
        '####.#...#',
        '##.##.###.',
        '##...#.###',
        '.#.#.#..##',
        '..#....#..',
        '###...#.#.',
        '..###..###',
        '',
        'Tile 1951:',
        '#.##...##.',
        '#.####...#',
        '.....#..##',
        '#...######',
        '.##.#....#',
        '.###.#####',
        '###.##.##.',
        '.###....#.',
        '..#.#..#.#',
        '#...##.#..',
        '',
        'Tile 1171:',
        '####...##.',
        '#..##.#..#',
        '##.#..#.#.',
        '.###.####.',
        '..###.####',
        '.##....##.',
        '.#...####.',
        '#.##.####.',
        '####..#...',
        '.....##...',
        '',
        'Tile 1427:',
        '###.##.#..',
        '.#..#.##..',
        '.#.##.#..#',
        '#.#.#.##.#',
        '....#...##',
        '...##..##.',
        '...#.#####',
        '.#.####.#.',
        '..#..###.#',
        '..##.#..#.',
        '',
        'Tile 1489:',
        '##.#.#....',
        '..##...#..',
        '.##..##...',
        '..#...#...',
        '#####...#.',
        '#..#.#.#.#',
        '...#.#.#..',
        '##.#...##.',
        '..##.##.##',
        '###.##.#..',
        '',
        'Tile 2473:',
        '#....####.',
        '#..#.##...',
        '#.##..#...',
        '######.#.#',
        '.#...#.#.#',
        '.#########',
        '.###.#..#.',
        '########.#',
        '##...##.#.',
        '..###.#.#.',
        '',
        'Tile 2971:',
        '..#.#....#',
        '#...###...',
        '#.#.###...',
        '##.##..#..',
        '.#####..##',
        '.#..####.#',
        '#..#.#..#.',
        '..####.###',
        '..#.#.###.',
        '...#.#.#.#',
        '',
        'Tile 2729:',
        '...#.#.#.#',
        '####.#....',
        '..#.#.....',
        '....#..#.#',
        '.##..##.#.',
        '.#.####...',
        '####.#.#..',
        '##.####...',
        '##..#.##..',
        '#.##...##.',
        '',
        'Tile 3079:',
        '#.#.#####.',
        '.#..######',
        '..#.......',
        '######....',
        '####.#..#.',
        '.#...#.##.',
        '#.#####.##',
        '..#.###...',
        '..#.......',
        '..#.###...'
    ]) == 20899048083289

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
