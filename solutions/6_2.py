raw_grid = []
raw_operators = []
with open("./inputs/6.txt") as file:
    raw_lines = file.readlines()
    for i in range(len(raw_lines)):
        if i == len(raw_lines) - 1:
            raw_operators = list(raw_lines[i].strip())
        else:
            # We can't just strip because we need to preserve whitespace cols on ends
            if raw_lines[i][-1] == "\n":
                raw_lines[i] = raw_lines[i][: len(raw_lines[i]) - 1]
            raw_grid.append(list(raw_lines[i]))


operators = []
for char in raw_operators:
    if char != " ":
        operators.append(char)


parts = []
current_parts = []
for col in range(len(raw_grid[0])):
    is_break = True
    for row in range(len(raw_grid)):
        if raw_grid[row][col] != " ":
            is_break = False
    if is_break:
        parts.append(current_parts)
        current_parts = []
        continue
    num = ""
    for row in range(len(raw_grid)):
        num += raw_grid[row][col]
    current_parts.append(int(num))
parts.append(current_parts)


total = 0
for i in range(len(parts)):
    answer = 0 if operators[i] == "+" else 1
    for num in parts[i]:
        if operators[i] == "+":
            answer += num
        elif operators[i] == "*":
            answer *= num
        else:
            raise ValueError(f"Invalid operator {operators[i]} at index {i}")
    total += answer

print(total)
