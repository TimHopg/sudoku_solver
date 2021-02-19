# Back tracking algorithm
# 1. Pick empty square
# 2. Try all numbers
# 3. Find one that works
# 4. Repeat in next empty square
# 5. Backtrack when error encountered

grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

blank_grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]]


def print_grid(gr):
    for i in range(len(gr)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(gr[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")  # end="" means not default new line -> \n
            if j == 8:
                print(gr[i][j])
            else:
                print(str(gr[i][j]) + " ", end="")


# y & x -> position, across from left then down from top
# n -> number
def possible(x, y, n):
    global grid
    for i in range(0, 9):
        if grid[x][i] == n:
            return False
    for i in range(0, 9):
        if grid[i][y] == n:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[x0 + i][y0 + j] == n:
                return False
    return True


def solve():
    global grid

    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0:
                for n in range(1, 10):
                    if possible(x, y, n):
                        grid[x][y] = n
                        solve()
                        grid[x][y] = 0  # backtracking
                return
    print_grid(grid)
    input("Find another solution?")


print_grid(grid)
print()
solve()
print("There are no more solutions")
