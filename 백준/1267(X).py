import sys
input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
y_list, m_list = [], []
for i in num :
    y_num = i//30 + 1; m_num = i//60 + 1
    y_price = y_num*10; m_price = m_num*15
    y_list.append(y_price); m_list.append(m_price)
if sum(y_list) > sum(m_list) : print(f"M {sum(m_list)}")
elif sum(y_list) < sum(m_list) : print(f"Y {sum(y_list)}")
else : print(f"Y M {sum(m_list)}")

# https://www.acmicpc.net/problem/1267