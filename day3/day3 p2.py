import re

mul_instruction = re.compile(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)")

with open("adventofcode2024/day3/day3", "r") as file:
    matches = [match for match in mul_instruction.finditer(file.read())]

sum = 0
process = True
for item in matches:
    match item.group(0)[0:3]:
        case "do(":
            process = True
        case "don":
            process = False
        case "mul":
            if process:
                sum += int(item.group(1)) * int(item.group(2))

print(sum)