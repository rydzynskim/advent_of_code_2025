def dfs(layout, cache, current, target):
    if current == target:
        return 1

    if current == "out":
        return 0

    if current in cache:
        return cache[current]

    total = 0
    for child in layout[current]:
        total += dfs(layout, cache, child, target)

    cache[current] = total

    return total


layout = {}
with open("./inputs/11.txt") as file:
    raw_lines = file.readlines()
    for raw_line in raw_lines:
        device, raw_children = raw_line.strip().split(":")
        children = raw_children.strip().split(" ")
        layout[device] = set(children)

svr_to_fft = dfs(layout, {}, "svr", "fft")
fft_to_dac = dfs(layout, {}, "fft", "dac")
dac_to_out = dfs(layout, {}, "dac", "out")
print(svr_to_fft * fft_to_dac * dac_to_out)
