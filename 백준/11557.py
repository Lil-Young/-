T = int(input())
for i in range(T) :
    N = int(input())
    dic = {}
    for j in range(N) :
        S, L = map(str, input().split())
        L = int(L)
        dic[S] = L
    data = max(dic.values())
    reverse_dic = dict(map(reversed, dic.items()))
    print(reverse_dic[data])