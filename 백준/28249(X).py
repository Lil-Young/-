import sys
input = sys.stdin.readline
dic = {"Poblano":1500, "Mirasol":6000, "Serrano":15500, "Cayenne":40000, "Thai":75000, "Habanero":125000}
sum = 0
for i in range(int(input())):
    word = input().rstrip()
    sum += dic[word]
print(sum)

# https://www.acmicpc.net/problem/28249