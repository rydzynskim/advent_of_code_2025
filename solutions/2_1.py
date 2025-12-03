def invalid(num):
    n = len(num)
    if n % 2 == 1:
        return False
    return num[n // 2 :] == num[: n // 2]


ranges = []
with open("./inputs/2.txt") as file:
    for raw_range in file.read().split(","):
        raw_start, raw_end = raw_range.split("-")
        ranges.append((int(raw_start), int(raw_end)))

sum = 0
for [start, end] in ranges:
    for num in range(start, end + 1):
        if invalid(str(num)):
            sum += num

print(sum)
