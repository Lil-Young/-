import sys
input = sys.stdin.readline
N,M = map(int, input().split())
nums = list(map(int, input().split()))
arr = []
for i in range(len(nums)-2) :
    for j in range(i+1, len(nums)-1) :
        for k in range(i+2, len(nums)) :
            if i!=j!=k and nums[i] + nums[j] + nums[k] <= M:
                arr.append(nums[i] + nums[j] + nums[k])
print(max(arr))