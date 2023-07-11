import sys
input = sys.stdin.readline
X = int(input())
fix_X = X
count = 0
num = 0
count_list = []
while True:
    if num == 0:
        count+=1
        if X%3 == 0: X//=3
        elif X%2 == 0: X//=2
        else: X-=1
        if X == 1: count_list.append(count); count = 0; num+=1
    elif num == 1:
        if count== 0: X = fix_X
        count+=1
        if X%3 == 0: X//=3
        else: X-=1
        if X%2 == 0: X//=2
        if X == 1: count_list.append(count); count = 0; num+=1
    elif num == 2:
        if count== 0: X = fix_X
        count+=1
        if X%2 == 0: X//=2
        elif X%3 == 0: X//=3
        else: X-=1
        if X == 1: count_list.append(count); count = 0; num+=1
    elif num == 3:
        if count== 0: X = fix_X
        count+=1
        if X%2 == 0: X//=2
        else: X-=1
        if X%3 == 0: X//=3
        if X == 1: count_list.append(count); count = 0; num+=1
    elif num == 4:
        if count== 0: X = fix_X
        count+=1
        X-=1
        if X%3 == 0: X//=3
        elif X%2 == 0: X//=2
        else: continue
        if X == 1: count_list.append(count); count = 0; num+=1
    elif num == 5:
        if count== 0: X = fix_X
        X = fix_X
        count+=1
        X-=1
        if X%2 == 0: X//=2
        elif X%3 == 0: X//=3
        if X == 1: count_list.append(count); count = 0; num+=1
    if num == 6: break    
print(min(count_list))
    
    

# https://www.acmicpc.net/problem/1463