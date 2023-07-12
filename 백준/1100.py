import sys
input = sys.stdin.readline
word = [input().rstrip() for _ in range(8)]
num = 0
for i in range(8):
    if i%2== 0:
        for j in range(0, len(word), 2) :
            if word[i][j] == "F":
                num += 1
    else : 
        for k in range(1, len(word), 2):
            if word[i][k] == "F":
                num += 1

print(num)