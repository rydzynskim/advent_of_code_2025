def invalid(num):
    n = len(num)
    for i in range(1, n // 2 + 1):
        is_valid = True
        sub_1 = num[:i]
        for j in range(0, n, i):
            sub_2 = num[j : j + i]
            if sub_1 != sub_2:
                is_valid = False
                break
        if is_valid:
            return True
    return False


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
