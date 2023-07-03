import sys
input = sys.stdin.readline
N = set(input().rstrip()); N = list(N)
if "M" in N and 'O' in N and'I' in N and'S' in N and'B' in N: print("YES")
else: print("NO")