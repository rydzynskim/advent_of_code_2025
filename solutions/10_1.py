def lights_to_dec(lights: str) -> int:
    dec = 0
    for i in range(len(lights)):
        if lights[len(lights) - 1 - i] == "#":
            dec += 2**i
    return dec


def dec_to_lights(dec: int, size: int) -> str:
    bin = ""
    while dec > 0:
        bin += str(dec % 2)
        dec //= 2

    res = ""
    for i in range(size):
        if i < len(bin):
            res = ("#" if bin[i] == "1" else ".") + res
        else:
            res = "." + res

    return res


def press_button(dec: int, size: int, button: list) -> int:
    lights = list(dec_to_lights(dec, size))
    for num in button:
        lights[num] = "." if lights[num] == "#" else "#"
    return lights_to_dec("".join(lights))


def construct_graph(size: int, buttons: list[list[int]]) -> list[list[int]]:
    graph = []
    for _ in range(2**size + 1):
        row = []
        for _ in range(2**size + 1):
            row.append(0)
        graph.append(row)

    for i in range(len(graph)):
        for button in buttons:
            graph[i][press_button(i, size, button)] = 1

    return graph


def bfs(target: str, graph: list[list[int]]) -> dict[str, str]:
    previous = {dec_to_lights(0, len(target)): None}
    current = [0]
    while target not in previous:
        next = []
        for c in current:
            for i in range(len(graph[c])):
                c_light = dec_to_lights(c, len(target))
                n_light = dec_to_lights(i, len(target))
                if graph[c][i] == 1 and n_light not in previous:
                    previous[n_light] = c_light
                    next.append(i)
        current = next

    return previous


def construct_path(previous: dict[str, str], target: str) -> int:
    current = target
    count = 0
    while current != None:
        current = previous[current]
        count += 1

    return count - 1


lights = []
buttons = []
with open("./inputs/10.txt") as file:
    raw_lines = file.readlines()
    for raw_line in raw_lines:
        splits = raw_line.strip().split(" ")
        current_buttons = []
        for i in range(len(splits)):
            current_machine = [[], []]
            if i == len(splits) - 1:
                continue
            elif i == 0:
                lights.append(splits[i][1:-1])
            else:
                button_scheme = []
                for num in splits[i][1:-1].split(","):
                    button_scheme.append(int(num))
                current_buttons.append(button_scheme)
        buttons.append(current_buttons)


total = 0
for i in range(len(lights)):
    graph = construct_graph(len(lights[i]), buttons[i])
    previous = bfs(lights[i], graph)
    total += construct_path(previous, lights[i])

print(total)
