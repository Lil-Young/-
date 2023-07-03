a, b, c = map(int, input().split())
list1 = []
list1.append(a); list1.append(b); list1.append(c)
max_num = max(list1)
min_num = min(list1)
result = 0
for i in range(len(list1)) :
    if list1[i] < max_num and list1[i] > min_num :
        result = list1[i]
        print(result)
if result == 0 :
    if list1.count(max_num) == 2 :
        print(max_num)
    else :
        print(min_num)
