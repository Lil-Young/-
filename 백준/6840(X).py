import sys
input = sys.stdin.readline
a = int(input())
b = int(input())
c = int(input())
total = []; total.extend([a, b, c]); total.remove(max(total)); total.remove(min(total))
print(total[0])

# https://www.acmicpc.net/problem/6840