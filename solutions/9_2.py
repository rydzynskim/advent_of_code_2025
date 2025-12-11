# Disclaimer for this one. I knew the general algorithm I needed here:
# - fill in edges of polygon
# - bfs to find all points within
# - only take rectangles where all edges are within polygon
# However, I couldn't get it to run in reasonable amount of time.
# I ended up looking up a hint on the subreddit, which is where I
# discovered the coordinate compression piece. I'll know next time!


def s(p):
    return f"{p[0]},{p[1]}"


def next_points(p):
    return [
        (p[0] - 1, p[1] - 1),
        (p[0] - 1, p[1]),
        (p[0] - 1, p[1] + 1),
        (p[0], p[1] - 1),
        (p[0], p[1] + 1),
        (p[0] + 1, p[1] - 1),
        (p[0] + 1, p[1]),
        (p[0] + 1, p[1] + 1),
    ]


def fill(p, q):
    points = set()
    for x in range(min(p[0], q[0]), max(p[0], q[0]) + 1):
        points.add(s((x, p[1])))
    for y in range(min(p[1], q[1]), max(p[1], q[1]) + 1):
        points.add(s((p[0], y)))
    return points


def area(p, q):
    width = abs(p[0] - q[0]) + 1
    height = abs(p[1] - q[1]) + 1
    return width * height


def compress(points):
    original_x = []
    original_y = []
    for p in points:
        original_x.append(p[0])
        original_y.append(p[1])

    original_x_deduped = set(original_x)
    original_x_sorted = list(original_x_deduped)
    original_x_sorted.sort()
    original_y_deduped = set(original_y)
    original_y_sorted = list(original_y_deduped)
    original_y_sorted.sort()

    x_map = {}
    i = 1
    for x in original_x_sorted:
        x_map[x] = i
        i += 1

    y_map = {}
    i = 1
    for y in original_y_sorted:
        y_map[y] = i
        i += 1

    compressed_points = []
    for p in points:
        compressed_points.append((x_map[p[0]], y_map[p[1]]))

    return compressed_points


points = []
with open("./inputs/9.txt") as file:
    raw_lines = file.readlines()
    for raw_line in raw_lines:
        x, y = raw_line.strip().split(",")
        points.append((int(x), int(y)))
points.append(points[0])
compressed_points = compress(points)


outside = set()
for i in range(len(compressed_points) - 1):
    c = compressed_points[i]
    n = compressed_points[i + 1]
    outside = outside.union(fill(c, n))


start = (120, 80)  # got this through graphing points and picking one inside
inside = set([s(start)])
current = [start]
while len(current) > 0:
    next = []
    for point in current:
        for child in next_points(point):
            serialized = s(child)
            if serialized not in outside and serialized not in inside:
                inside.add(serialized)
                next.append(child)
    current = next


polygon = inside.union(outside)
max_area = -1
for i in range(len(compressed_points)):
    for j in range(len(compressed_points)):
        first = compressed_points[i]
        second = compressed_points[j]
        s1 = fill(first, (first[0], second[1]))
        s2 = fill(first, (second[0], first[1]))
        s3 = fill((first[0], second[1]), second)
        s4 = fill((second[0], first[1]), second)
        perimeter = s1.union(s2).union(s3).union(s4)

        valid = True
        for p in perimeter:
            if p not in polygon:
                valid = False
                break

        if valid:
            a = area(points[i], points[j])
            if a > max_area:
                max_area = a

print(max_area)
