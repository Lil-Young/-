a, b, c = map(int, input().split())
if a == b == c :
    print(10000+a*1000)
elif a == b or a == c or b == c :
    if a == b or a == c :
        print(1000+a*100)
    elif c == a or c == b :
        print(1000+c*100)
else :
    print(100 * max(a, b, c))