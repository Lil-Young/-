import sys
input = sys.stdin.readline
word = list(input().rstrip().split('/'))
k, d, a = int(word[0]), int(word[1]), int(word[2])
if k+a < d or d == 0: print("hasu")
else: print("gosu")

# https://www.acmicpc.net/problem/20499