import os.path as path


def can_be_constructed(n: int, l: list[str]) -> bool:
    if (len(l) == 1):
        return (l[0] == n)
    if (can_be_constructed(n, [l[0] + l[1]] + l[2:])):
        return True
    if (can_be_constructed(n, [l[0] * l[1]] + l[2:])):
        return True
    if (can_be_constructed(n, [int(str(l[0]) + str(l[1]))] + l[2:])):
        return True
    else:
        return False


with open(path.dirname(__file__) + "/input", 'r') as file:
    values = []
    for line in file.readlines():
        left, right = line.split(":")
        left = int(left)
        right = [int(n) for n in right.strip().split(" ")]
        values.append((left, right))

sum = 0

for value in values:
    if can_be_constructed(value[0], value[1]):
        sum += value[0]

print(sum)