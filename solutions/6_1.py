def parse_line(raw_line):
    output = []
    current = ""
    raw_line = raw_line.strip() + " "
    for char in raw_line:
        if char == " ":
            if len(current) > 0:
                output.append(current)
                current = ""
            continue
        current += char
    return output


parts = []
operators = []
with open("./inputs/6.txt") as file:
    raw_lines = file.readlines()
    for i in range(len(raw_lines)):
        if i == len(raw_lines) - 1:
            operators = parse_line(raw_lines[i])
        else:
            parts.append(parse_line(raw_lines[i]))

total = 0
for i in range(len(parts[0])):
    answer = 0 if operators[i] == "+" else 1
    for j in range(len(parts)):
        if operators[i] == "+":
            answer += int(parts[j][i])
        elif operators[i] == "*":
            answer *= int(parts[j][i])
        else:
            raise ValueError(f"Invalid operator {operators[i]} at index {i}")
    total += answer

print(total)
