T = int(input())
for i in range(T) :
    a = list(map(str, input().split()))
    a[0] = float(a[0])
    result = a[0]
    for j in range(1, len(a)) :
        if a[j] == '@' :
            result *= 3
        elif a[j] == '%' :
            result += 5
        elif a[j] == '#' :
            result -= 7
    print("%.2lf" %result)
