ranges = []
with open("./inputs/5.txt") as file:
    raw_lines = file.readlines()
    seen_empty = False
    for raw_line in raw_lines:
        if raw_line.strip() == "":
            break

        start, end = raw_line.strip().split("-")
        ranges.append([int(start), int(end)])

ranges.sort(key=lambda x: x[0])
combined_ranges = [[ranges[0][0], ranges[0][1]]]
for start, end in ranges[1:]:
    if combined_ranges[len(combined_ranges) - 1][1] >= start:
        combined_ranges[len(combined_ranges) - 1][1] = max(
            combined_ranges[len(combined_ranges) - 1][1], end
        )
    else:
        combined_ranges.append([start, end])

count = 0
for start, end in combined_ranges:
    count += end - start + 1

print(count)
