import sys
input = sys.stdin.readline
a, b = map(int, input().split())
new_a, new_b = 100-a, 100-b
c = 100 - (new_a+new_b)
d = new_a*new_b
(q, r) = divmod(d, 100)
head, tail  = c+q, r
print(new_a, new_b, c, d, q, r)
print(head, tail)

# https://www.acmicpc.net/problem/25591