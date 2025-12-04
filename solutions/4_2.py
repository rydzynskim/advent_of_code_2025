def valid(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])


def surrounding(grid, row, col):
    surrounding = 0
    if valid(grid, row - 1, col - 1) and grid[row - 1][col - 1] == "@":
        surrounding += 1
    if valid(grid, row - 1, col) and grid[row - 1][col] == "@":
        surrounding += 1
    if valid(grid, row - 1, col + 1) and grid[row - 1][col + 1] == "@":
        surrounding += 1
    if valid(grid, row, col - 1) and grid[row][col - 1] == "@":
        surrounding += 1
    if valid(grid, row, col + 1) and grid[row][col + 1] == "@":
        surrounding += 1
    if valid(grid, row + 1, col - 1) and grid[row + 1][col - 1] == "@":
        surrounding += 1
    if valid(grid, row + 1, col) and grid[row + 1][col] == "@":
        surrounding += 1
    if valid(grid, row + 1, col + 1) and grid[row + 1][col + 1] == "@":
        surrounding += 1
    return surrounding


grid = []
with open("./inputs/4.txt") as file:
    raw_rows = file.readlines()
    for raw_row in raw_rows:
        grid.append(list(raw_row.strip()))

total = 0
while True:
    removed_positions = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == ".":
                continue
            if surrounding(grid, row, col) < 4:
                removed_positions.append((row, col))

    if len(removed_positions) == 0:
        break

    total += len(removed_positions)
    for row, col in removed_positions:
        grid[row][col] = "."


print(total)
