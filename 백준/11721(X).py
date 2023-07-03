import sys
input = sys.stdin.readline
word = input().rstrip()
result = [word[i:i+10] for i in range(0, len(word), 10)]
for i in result :
    print(i)
    
# https://www.acmicpc.net/problem/11721