import sys
input = sys.stdin.readline
# N: 여학생, M: 남학생, K: 인턴쉽참여수
N, M, K = map(int, input().split())
_list = []
for i in range(K+1):
    n, m, k = N, M, K
    n -= i
    k -= i
    m -= k
    if n <= 0 or m <= 0: pass
    else:
        if n//2 <= m: _list.append(n//2)
        else: _list.append(m)
print(max(_list))