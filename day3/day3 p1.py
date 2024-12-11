import re

mul_instruction = re.compile(r"mul\((\d+),(\d+)\)")

strings = []
with open("adventofcode2024/day3/day3", "r") as file:
    strings = file.readlines()

sum = 0
for s in strings:
    for pair in mul_instruction.findall(s):
        sum += int(pair[0]) * int(pair[1])

print(sum)