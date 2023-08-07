import sys
input = sys.stdin.readline
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
F = int(input())

total_list, list_4, list_2  = [], [], []
list_4.extend([A, B, C, D])
list_2.extend([E, F])
list_4.remove(min(list_4))
list_2.remove(min(list_2))
total_list.extend([list_4, list_2])
total = 0
for i in range(2) :
    for j in total_list[i] :
        total += j
print(total)