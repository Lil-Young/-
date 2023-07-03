import sys
input = sys.stdin.readline
while True:
    word = input().rstrip()
    if word == "#":
        break
    word = word.lower()
    total = 0
    total += word.count('a')
    total += word.count('e')
    total += word.count('i')
    total += word.count('o')
    total += word.count('u')
    print(total)
    
# https://www.acmicpc.net/problem/1264