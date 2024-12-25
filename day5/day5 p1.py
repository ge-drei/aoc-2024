import os.path as path

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
    valid_report = True
    for n in report:
        # If a rule was brought in by the second number, and the first number now appears:
        if any(rule[0] == n for rule in relevant_rules):
            valid_report = False
            break
        for rule in rules:
            if (n in rule):
                relevant_rules.add(tuple(rule))
    if (valid_report):
        count += report[len(report) // 2]

print(count)