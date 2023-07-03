a = input()
num = 0
if len(a) == 2 :
    for i in a :
        num += int(i)
elif len(a) == 3 :
    if a[1] == '0':
        num = int(a[:2]) + int(a[2])
    elif a[2] == '0':
        num = int(a[1:]) + int(a[0])
elif a[1] == '0' and a[3] == '0':
    num = int(a[:2]) + int(a[2:])
print(num)

# https://www.acmicpc.net/problem/15873