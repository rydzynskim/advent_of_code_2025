ranges = []
ingredients = []
with open("./inputs/5.txt") as file:
    raw_lines = file.readlines()
    seen_empty = False
    for raw_line in raw_lines:
        if raw_line.strip() == "":
            seen_empty = True
            continue

        if seen_empty:
            ingredients.append(int(raw_line.strip()))
        else:
            start, end = raw_line.strip().split("-")
            ranges.append([int(start), int(end)])


count = 0
for i in ingredients:
    is_fresh = False
    for start, end in ranges:
        if start <= i <= end:
            is_fresh = True
            break

    if is_fresh:
        count += 1


print(count)
