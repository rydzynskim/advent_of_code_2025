lines = []
with open("./inputs/1.txt") as file:
    lines = file.readlines()

dial = 50
zero_count = 0
for line in lines:
    amount = int(line[1:])
    if line[0] == "L":
        amount *= -1

    prev_zero = dial == 0
    dial += amount
    if dial == 0 and not prev_zero:
        zero_count += 1
    elif dial < 0:
        zero_count += (-1 * dial) // 100 + (0 if prev_zero else 1)
    elif dial > 99:
        zero_count += dial // 100
    dial %= 100


print(zero_count)
