import os.path as path

def is_record_safe(Record: list, can_remove: bool = True):
    record = Record.copy()
    decreasing = True if (record[0] > record[1]) else False
    increasing = not decreasing
    
    for i in range(len(record) - 1):
        if ((decreasing and record[i+1] > record[i]) or
            (increasing and record[i] > record[i+1]) or
            not (1 <= abs(record[i] - record[i+1]) <= 3)):

            if can_remove:
                for j in [-1, 0, 1]:
                    subrecord = record.copy()
                    subrecord.pop(max(0, min(i + j, len(record))))
                    if is_record_safe(subrecord, False):
                        return True    
            return False
    return True


reports = []
with open(path.dirname(__file__) + "/input", "r") as file:
    for line in file:
        reports.append(list([int(level) for level in line.split()]))

num_safe = 0

for report in reports:
    if is_record_safe(report):
        num_safe += 1

print(num_safe)