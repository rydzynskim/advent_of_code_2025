def hash(row, col):
    return f"{row},{col}"


def dfs(grid, cache, row, col):
    if row == len(grid):
        return 1

    if hash(row, col) in cache:
        return cache[hash(row, col)]

    ret = -1
    if grid[row][col] == "^":
        ret = dfs(grid, cache, row + 1, col - 1) + dfs(grid, cache, row + 1, col + 1)
    else:
        ret = dfs(grid, cache, row + 1, col)
    cache[hash(row, col)] = ret

    return ret


grid = []
with open("./inputs/7.txt") as file:
    raw_lines = file.readlines()
    for raw_line in raw_lines:
        grid.append(list(raw_line.strip()))


start_column = -1
for i in range(len(grid[0])):
    if grid[0][i] == "S":
        start_column = i

print(dfs(grid, {}, 0, start_column))
