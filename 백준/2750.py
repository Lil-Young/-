N = int(input())
arr = []
for _ in range(N) :
    val = int(input())
    arr.append(val)
arr.sort()
for i in arr :
    print(i)