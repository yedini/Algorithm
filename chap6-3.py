N = int(input())

students = dict()
for i in range(N):
    n = list(input().split())
    students[n[0]] = int(n[1])

students = dict(sorted(students.items(),  key = lambda item: item[1]))
names = students.keys()
print(" ".join(names))