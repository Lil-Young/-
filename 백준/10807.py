import sys
input = sys.stdin.readline
N = int(input())
_list = list(map(int, input().rstrip().split()))
num = int(input())
print(_list.count(num))