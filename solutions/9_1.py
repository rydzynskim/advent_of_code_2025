points = []
with open("./inputs/9.txt") as file:
    raw_lines = file.readlines()
    for raw_line in raw_lines:
        x, y = raw_line.strip().split(",")
        points.append((int(x), int(y)))

max = -1
for a in points:
    for b in points:
        width = abs(a[0] - b[0]) + 1
        height = abs(a[1] - b[1]) + 1
        area = width * height
        if area > max:
            max = area
print(max)
