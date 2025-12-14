def dfs(layout, current, path):
    if current == "out":
        return 1

    total = 0
    for child in layout[current]:
        if child not in path:
            updated_path = path.copy()
            updated_path.add(child)
            total += dfs(layout, child, updated_path)

    return total


layout = {}
with open("./inputs/11.txt") as file:
    raw_lines = file.readlines()
    for raw_line in raw_lines:
        device, raw_children = raw_line.strip().split(":")
        children = raw_children.strip().split(" ")
        layout[device] = set(children)

print(dfs(layout, "you", set()))
