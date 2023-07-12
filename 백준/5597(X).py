import sys
input = sys.stdin.readline
students = [i for i in range(1, 31)]
for i in range(28):
    a = int(input())
    students.remove(a)
print(students[0])
print(students[1])

# https://www.acmicpc.net/problem/5597