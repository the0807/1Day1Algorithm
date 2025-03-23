# 5597번 "과제 안 내신 분..?"

students = [i for i in range(1, 31)]

for _ in range(28):
    a = int(input())
    students.remove(a)

print(min(students))
print(max(students))