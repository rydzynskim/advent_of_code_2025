DIGITS = [
    "9",
    "8",
    "7",
    "6",
    "5",
    "4",
    "3",
    "2",
    "1",
]


def has_enough_to_right(bank, index, amount):
    return len(bank) - index - 1 >= amount


def largest(bank, remaining):
    if remaining == 0:
        return ""

    for digit in DIGITS:
        found_index = -1
        for i in range(len(bank)):
            if digit == bank[i] and has_enough_to_right(bank, i, remaining - 1):
                found_index = i
                break
        if found_index != -1:
            return bank[found_index] + largest(
                bank[found_index + 1 :],
                remaining - 1,
            )

    raise ValueError(f"Should not get here, {bank, remaining}")


banks = []
with open("./inputs/3.txt") as file:
    banks = file.readlines()
    for i in range(len(banks)):
        banks[i] = banks[i].strip()


sum = 0
for bank in banks:
    sum += int(largest(bank, 12))

print(sum)
