lines = []
with open("./inputs/1.txt") as file:
    lines = file.readlines()

dial = 50
zero_count = 0
for line in lines:
    amount = int(line[1:]) % 100
    if line[0] == "L":
        amount *= -1

    dial += amount
    if dial < 0:
        dial = 100 + dial
    elif dial > 99:
        dial = dial - 100

    if dial == 0:
        zero_count += 1

print(zero_count)
