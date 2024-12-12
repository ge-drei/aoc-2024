import re
import os.path as path

mul_instruction = re.compile(r"mul\((\d+),(\d+)\)")

strings = []
with open(path.dirname(__file__) + "/input", "r") as file:
    strings = file.readlines()

sum = 0
for s in strings:
    for pair in mul_instruction.findall(s):
        sum += int(pair[0]) * int(pair[1])

print(sum)