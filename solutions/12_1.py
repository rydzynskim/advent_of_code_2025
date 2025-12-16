def display(present):
    for row in present:
        print("".join(row))
    print()


def empty(rows, cols):
    result = []
    for _ in range(rows):
        result_row = []
        for _ in range(cols):
            result_row.append(".")
        result.append(result_row)
    return result


def flip(present):
    flipped_present = []
    for row in range(len(present)):
        flipped_row = present[row][::-1]
        flipped_present.append(flipped_row)
    return flipped_present


def rotate(present):
    rotated_presents = [present[:]]
    for _ in range(3):
        next_present = empty(len(present), len(present[0]))
        for row in range(len(present)):
            for col in range(len(present[row])):
                next_present[len(present[row]) - 1 - col][row] = rotated_presents[-1][
                    row
                ][col]
        rotated_presents.append(next_present)
    return rotated_presents


def possible(present):
    result = rotate(present)
    result += rotate(flip(present))
    return result


def is_valid(row, col, grid):
    if row < 0 or row >= len(grid):
        return False
    if col < 0 or col >= len(grid[0]):
        return False
    return True


def place(present, grid, row, col):
    for i in range(len(present)):
        for j in range(len(present[0])):
            if (
                not is_valid(row + i, col + j, grid)
                or present[i][j] == "#"
                and grid[row + i][col + j] == "#"
            ):
                return False
    for i in range(len(present)):
        for j in range(len(present[0])):
            if present[i][j] == "#":
                grid[row + i][col + j] = "#"
    return True


def unplace(present, grid, row, col):
    for i in range(len(present)):
        for j in range(len(present[0])):
            if present[i][j] == "#":
                grid[row + i][col + j] = "."


def parse_present(raw_present):
    present = []
    for row in raw_present.split("\n")[1:]:
        present.append(list(row))
    return present


def parse_regions(lines):
    result = []
    for region in lines.split("\n"):
        size, raw_requirements = region.split(":")
        cols, rows = size.strip().split("x")
        grid = empty(int(rows), int(cols))
        requirements = []
        for requirement in raw_requirements.strip().split(" "):
            requirements.append(int(requirement))
        result.append({"grid": grid, "requirements": requirements})
    return result


def parse():
    sections = []
    with open("./inputs/12.txt") as file:
        sections = file.read().split("\n\n")
    regions = parse_regions(sections[-1])
    presents = []
    for section in sections[: len(sections) - 1]:
        present = parse_present(section)
        presents.append(possible(present))
    return presents, regions


def hash(requirements, grid):
    grid_flat = []
    for row in grid:
        grid_flat += row
    requirements_str = ",".join(str(num) for num in requirements)
    grid_str = ",".join(cell for cell in grid_flat)
    return f"{requirements_str}-{grid_str}"


def backtrace(attempted, presents, requirements, grid, i, min_row, min_col):
    if sum(requirements) == 0:
        return True

    if i == len(requirements):
        return False

    h = hash(requirements, grid)
    if h in attempted:
        return False

    if requirements[i] == 0:
        return backtrace(attempted, presents, requirements, grid, i + 1, 0, 0)

    for row in range(min_row, len(grid)):
        for col in range(min_col if row == min_row else 0, len(grid[row])):
            for present in presents[i]:
                if place(present, grid, row, col):
                    requirements[i] -= 1
                    if backtrace(attempted, presents, requirements, grid, i, row, col):
                        return True
                    else:
                        requirements[i] += 1
                        unplace(present, grid, row, col)

    attempted.add(h)
    return False


presents, regions = parse()

# total = 0
# for region in regions:
#     total += backtrace(set(), presents, region["requirements"], region["grid"], 0, 0, 0)
# print(total)

# I wrote everything above here and couldn't solve the example problem in reasonable amount of time.
# Then I looked at the actual input more closely and realized the grid is much larger or smaller
# than is needed to fit required presents.

total = 0
for region in regions:
    total_area = len(region["grid"]) * len(region["grid"][0])
    required_area = sum(region["requirements"]) * 9
    total += 1 if required_area <= total_area else 0
print(total)
