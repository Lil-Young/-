# 파스칼의 삼각형 / D2

T = int(input())
for i in range(1, T+1):
    N = int(input())
    pascal = [[1]]
    for j in range(N-1):
        if len(pascal[j])%2 == 1:
            if len(pascal[j]) == 1:
                val = [1, 1]
            else:
                idx = len(pascal[j])//2
                val = pascal[j].copy()
                val[idx] = pascal[j][idx]+pascal[j][idx+1]
                val.insert(idx, pascal[j][idx]+pascal[j][idx+1])
        else:
            idx = len(pascal[j])//2
            val = pascal[j].copy()
            val.insert(idx, pascal[j][idx]+pascal[j][idx-1])
        pascal.append(val)
        
    print(f"#{i}")
    for r in pascal:
        for a in r:
            print(a, end=' ')
        print()