# # 단순 2진 암호코드 / D3

dic = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9}
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        v = list(input())
        if "1" in v:
            arr.append(v)
    a = arr[0]
    a.reverse()
    one = a.index("1")
    a = a[one:]
    b = []
    for i in range(0, len(a), 7):
          v = ''.join(reversed(a[i:i+7]))
          if v in dic.keys():
               b.append(dic[v])
    b.reverse()
    odd = [b[x] for x in range(0, len(b), 2)]
    even = [b[x] for x in range(1, len(b), 2)]
    if (sum(odd) * 3 + sum(even))%10 == 0:
         print(f"#{tc} {sum(odd)+sum(even)}")
    else:
         print(f"#{tc} {0}")
    # 0111011 0110001 0111011 0110001 0110001 0001101 0010011 0111011