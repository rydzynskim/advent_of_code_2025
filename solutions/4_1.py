def valid(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])


grid = []
with open("./inputs/4.txt") as file:
    raw_rows = file.readlines()
    for raw_row in raw_rows:
        grid.append(list(raw_row.strip()))

accessible = 0
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == ".":
            continue
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
        if surrounding < 4:
            accessible += 1

print(accessible)
