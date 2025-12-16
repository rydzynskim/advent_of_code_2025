import z3

# I was planning on not using any libraries, but I decided to use a solver
# here instead of writing one from scratch. Maybe there is a clever trick
# to this problem that I'm missing?

joltages = []
buttons = []
with open("./inputs/10.txt") as file:
    raw_lines = file.readlines()
    for raw_line in raw_lines:
        splits = raw_line.strip().split(" ")
        current_buttons = []
        for i in range(len(splits)):
            current_machine = [[], []]
            if i == 0:
                continue
            elif i == len(splits) - 1:
                joltage_scheme = []
                for joltage in splits[i][1:-1].split(","):
                    joltage_scheme.append(int(joltage))
                joltages.append(joltage_scheme)
            else:
                button_scheme = []
                for num in splits[i][1:-1].split(","):
                    button_scheme.append(int(num))
                current_buttons.append(button_scheme)
        buttons.append(current_buttons)


total = 0
for joltage in range(len(joltages)):
    solver = z3.Optimize()
    presses = z3.IntVector("presses", len(buttons[joltage]))

    # Bound number of presses for each button
    for button in range(len(buttons[joltage])):
        min = float("inf")
        for num in buttons[joltage][button]:
            if joltages[joltage][num] < min:
                min = joltages[joltage][num]
        solver.add(presses[button] >= 0)
        solver.add(presses[button] <= int(min))

    # Equality constraint
    for num in range(len(joltages[joltage])):
        included = set()
        for button in range(len(buttons[joltage])):
            if num in buttons[joltage][button]:
                included.add(button)

        sum = 0
        for i in included:
            sum += presses[i]
        solver.add(sum == joltages[joltage][num])

    # Solve it
    sum_presses = z3.Sum(presses)
    solver.minimize(sum_presses)
    solver.check()
    total += solver.model().eval(sum_presses).as_long()

print(total)
