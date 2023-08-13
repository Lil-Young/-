import sys
input = sys.stdin.readline
T = int(input())
A, B, C, D, E = map(int, input().split())
tea_list = [A, B, C, D, E]
print(tea_list.count(T))


# https://www.acmicpc.net/problem/11549