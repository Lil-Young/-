# 앨리스 A, 베토 B, 크랄라 C, 승자없으면 *
a = list(map(int, input().split()))
if 0 not in a or 1 not in a:
    result = None
elif a.count(0) > a.count(1):
    result = a.index(1)
elif a.count(0) < a.count(1):
    result = a.index(0)

if result == 0: print("A")
elif result == 1: print("B")
elif result == 2: print("C")
else: print("*")