def hash_single(a):
    return f"{a[0]},{a[1]},{a[2]}"


def hash_multiple(a, b):
    a_hash = f"{hash_single(a)}|{hash_single(b)}"
    b_hash = f"{hash_single(b)}|{hash_single(a)}"
    return a_hash if a_hash < b_hash else b_hash


def unhash(a):
    x, y, z = a.split(",")
    return (int(x), int(y), int(z))


def eql(a, b):
    return a[0] == b[0] and a[1] == b[1] and a[2] == b[2]


def dist(a, b):
    x = (a[0] - b[0]) ** 2
    y = (a[1] - b[1]) ** 2
    z = (a[2] - b[2]) ** 2
    return (x + y + z) ** (1 / 2)


points = []
with open("./inputs/8.txt") as file:
    raw_lines = file.readlines()
    for raw_line in raw_lines:
        points.append(unhash(raw_line.strip()))

seen = set()
distances = []
for a in points:
    for b in points:
        h = hash_multiple(a, b)
        if not eql(a, b) and h not in seen:
            distances.append((h, dist(a, b)))
            seen.add(h)
distances.sort(key=lambda x: x[1])


circuits = []
for i in range(1000):
    a, b = distances[i][0].split("|")
    a_circuit = None
    b_circuit = None
    for j in range(len(circuits)):
        if a in circuits[j]:
            a_circuit = j
        if b in circuits[j]:
            b_circuit = j
        if a_circuit != None and b_circuit != None:
            break

    if a_circuit == None and b_circuit == None:
        circuits.append(set([a, b]))
    elif a_circuit == None and b_circuit != None:
        circuits[b_circuit].add(a)
    elif a_circuit != None and b_circuit == None:
        circuits[a_circuit].add(b)
    elif a_circuit == b_circuit:
        continue
    else:
        circuits[a_circuit] = circuits[a_circuit].union(circuits[b_circuit])
        del circuits[b_circuit]
circuits.sort(key=lambda x: len(x), reverse=True)

print(len(circuits[0]) * len(circuits[1]) * len(circuits[2]))
