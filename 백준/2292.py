a = int(input())
num = 1
dt = 1
p = 6
while True :
    if num >= a :
        break
    num += p
    p += 6
    dt += 1
print(dt)