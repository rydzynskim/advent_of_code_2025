grid = []
with open("./inputs/7.txt") as file:
    raw_lines = file.readlines()
    for raw_line in raw_lines:
        grid.append(list(raw_line.strip()))


current_beams = []
for i in range(len(grid[0])):
    if grid[0][i] == "S":
        current_beams.append(i)


split_total = 0
row = 0
while row < len(grid):
    next_beams = set()
    for i in current_beams:
        if grid[row][i] == "^":
            split_total += 1
            next_beams.add(i - 1)
            next_beams.add(i + 1)
        else:
            next_beams.add(i)
    row += 1
    current_beams = list(next_beams)

print(split_total)
