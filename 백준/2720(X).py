import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    c = int(input())
    c_25 = c//25; c = c-(c_25*25)
    c_10 = c//10; c = c-(c_10*10)
    c_5 = c//5; c = c-(c_5*5)
    c_1 = c//1; c = c-(c_1*1)
    print(c_25, c_10, c_5, c_1)
    
# https://www.acmicpc.net/problem/2720