import sys
input = sys.stdin.readline
x = int(input())
first_x = x
cycle = 0
while True :
    if x < 10 :
        num = x
        x = x*10 + num
        cycle += 1
        if first_x == x :
            break
    else :
        num= x//10 + x%10
        if num < 10 :
            x = (x%10)*10 + num
        else :
            x = (x%10)*10 + num%10
        cycle += 1
        if first_x == x :
            break
print(cycle)
