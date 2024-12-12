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

similarity_score = 0

for i in list1:
    similarity_score += i * list2.count(i)

print(similarity_score)