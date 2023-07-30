import sys
input = sys.stdin.readline
asc_list = [1, 2, 3, 4, 5, 6, 7, 8]
desc_list = [8, 7, 6, 5, 4, 3, 2, 1]
num = list(map(int, input().split()))
if num == asc_list: print("ascending")
elif num == desc_list: print("descending")
else: print("mixed")
