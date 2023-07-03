import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    result = a % 10
    if result == 0:
        print(10)
    elif result == 1 or result == 5 or result == 6:
        print(result)
    elif result == 4 or result == 9:
        if b%2 == 0:
            print((result**2) % 10)
        else :
            print(result)
    else:
        if b%4 == 0:
            print((result**4) % 10)
        else:
            print(result**(b%4) % 10)
            