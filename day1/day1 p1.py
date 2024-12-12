import os.path as path

list1 = []
list2 = []
with open(path.dirname(__file__) + "/input", "r") as file:
    for line in file:
        num1, num2 = line.split()
        list1.append(int(num1))
        list2.append(int(num2))

list1.sort()
list2.sort()

total_distance = 0

for i in range(len(list1)):
    total_distance += abs(list1[i] - list2[i])

print(total_distance)