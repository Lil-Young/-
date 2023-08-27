import sys
input = sys.stdin.readline
for i in range(3):
    f_h, f_m, f_s, l_h, l_m, l_s = map(int, input().split())
    f_m = f_h*60+f_m; f_s = f_m*60+f_s
    l_m = l_h*60+l_m; l_s = l_m*60+l_s
    total_s = l_s - f_s
    result_s = total_s%60; result_m = total_s//60
    result_h = result_m//60; result_m = result_m%60
    print(result_h, result_m, result_s)