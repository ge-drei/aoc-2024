import os.path as path
from functools import cmp_to_key


def compare(x: int, y: int, rules: set) -> int:
    if any(x == rule[0] and y == rule[1] for rule in rules):
        return -1
    elif any(x == rule[1] and y == rule[0] for rule in rules):
        return 1
    else:
        return 0


rules = []
reports = []
with open(path.dirname(__file__) + "/input", 'r') as file:
    while(True):
        line = file.readline()
        if line == "\n":
            break
        else:
            rules += [[int(x) for x in line.strip().split('|')]]
    reports = [list(map(int, s.strip().split(','))) for s in file.readlines()]

count = 0
for report in reports:
    relevant_rules = set()
    invalid_report = False
    for n in report:
        # If a rule was brought in by the second number, and the first number now appears:
        if any(rule[0] == n for rule in relevant_rules):
            invalid_report = True
        for rule in rules:
            if (n in rule):
                relevant_rules.add(tuple(rule))
    if (invalid_report):
        # Rearrange to make valid
        # Trim rules
        trimmed_rules = set()
        for rule in relevant_rules:
            if all(n in report for n in rule):
                trimmed_rules.add(rule)
        # Sort list using rules
        report = sorted(report, key=cmp_to_key(lambda x, y: compare(x, y, trimmed_rules)))
        
        count += report[len(report) // 2]

print(count)