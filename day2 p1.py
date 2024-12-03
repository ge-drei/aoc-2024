def increasing_safely(l: list):
    all_increasing = all(l[i] < l[i+1] for i in range(len(l) - 1))
    all_steps_valid = all(1 <= abs(l[i+1] - l[i]) <= 3 for i in range(len(l) - 1))
    return (all_increasing and all_steps_valid)


def decreasing_safely(l: list):
    all_decreasing = all(l[i] > l[i+1] for i in range(len(l) - 1))
    all_steps_valid = all(1 <= abs(l[i+1] - l[i]) <= 3 for i in range(len(l) - 1))
    return (all_decreasing and all_steps_valid)


reports = []
with open("adventofcode2024/day2", "r") as file:
    for line in file:
        reports.append(list([int(level) for level in line.split()]))

num_safe = 0

for report in reports:
    if increasing_safely(report) or decreasing_safely(report):
        num_safe += 1

print(num_safe)