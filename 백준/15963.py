import sys
input = sys.stdin.readline
def equal(N, M):    
    if N == M :
        return 1
    else :
        return 0
N, M = map(int, input().split())
print(equal(N, M))