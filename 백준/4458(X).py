import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    word = input()
    print(word[0].upper()+word[1:])