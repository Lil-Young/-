T = int(input())
max_money = []
result = 0
for i in range(T) :
    a = []
    b, c, d = map(int, input().split())
    a.append(b); a.append(c); a.append(d)
    for j in range(len(a)) :
        if a.count(a[j]) == 3 :
            result = 10000 + a[j]*1000
        elif a.count(a[j]) == 2 :
            result = 1000 + a[j]*100
        else :
            result = max(a) *100
        max_money.append(result)
max_money = set(max_money)
print(max(max_money))