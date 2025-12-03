def largest(bank, index, current):
    if len(current) == 2:
        return int(current[0] + current[1])

    if index == len(bank):
        return -1

    n = current[:]
    n.append(bank[index])
    w = largest(bank, index + 1, n)
    wo = largest(bank, index + 1, current)

    return max(w, wo)


banks = []
with open("./inputs/3.txt") as file:
    banks = file.readlines()
    for i in range(len(banks)):
        banks[i] = banks[i].strip()

sum = 0
for bank in banks:
    sum += largest(bank, 0, [])

print(sum)
