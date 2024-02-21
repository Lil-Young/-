import sys
input = sys.stdin.readline
dic = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0}
a, b = 0, 0
for i in range(20):
    info = list(input().split())
    if info[2] == "P": pass
    else:
        a += float(info[1])*dic[info[2]]
        b += float(info[1])
print("%.6f" %(a/b))