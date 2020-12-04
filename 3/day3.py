def a(world, move=(3,1)):
    position = (0, 0)
    height = len(world)
    width = len(world[0])

    trees = 0
    while position[1] < height-1:
        position = (position[0]+move[0], position[1]+move[1])
        if world[position[1]][position[0]%width] == '#':
            trees +=1

    return trees

def b(world):
    res = 1
    for moves in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        res *= a(world, moves)
    return res

def test_a():
    assert a(["..##.......",
              "#...#...#..",
              ".#....#..#.",
              "..#.#...#.#",
              ".#...##..#.",
              "..#.##.....",
              ".#.#.#....#",
              ".#........#",
              "#.##...#...",
              "#...##....#",
              ".#..#...#.#"]) == 7

def test_b():
    assert b(["..##.......",
              "#...#...#..",
              ".#....#..#.",
              "..#.#...#.#",
              ".#...##..#.",
              "..#.##.....",
              ".#.#.#....#",
              ".#........#",
              "#.##...#...",
              "#...##....#",
              ".#..#...#.#"]) == 336
    
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
