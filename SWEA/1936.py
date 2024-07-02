# 1대1 가위바위보 / D1

# 가위 1, 바위 2, 보 3
A, B = map(int, input().split())
r = 'A' if A==1 and B==3 or A==2 and B==1 or A==3 or B==2 else 'B'
print(r)