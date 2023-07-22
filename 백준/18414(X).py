X, L, R = map(int, input().split())
num_list = [x for x in range(L, R+1)]
val = {}
for i in num_list:
    val[i] = abs(X-i)
min_val = min(list(val.values()))
convert_dict = {v:k for k, v in val.items()}
print(convert_dict[min_val])

# https://www.acmicpc.net/problem/18414