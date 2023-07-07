import sys
input = sys.stdin.readline
while True:
    _list = []
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0 : break
    _list.extend([a, b, c]); max_val = max(_list); _list.remove(max_val)
    if max_val >= sum(_list): print("Invalid")
    elif a == b and a == c and b == c: print("Equilateral")
    elif a != b and a != c and b != c: print("Scalene")
    else : print("Isosceles")
        
# https://www.acmicpc.net/problem/5073