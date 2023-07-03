while True :
    sum = 0
    n = int(input())
    if n == -1 :
        break
    for i in range(1, n) :
        if n%i == 0 :
            sum+=i
    if sum == n :
        print(n, "=", end = ' ')
        for i in range(1, n) :
            if n%i == 0 :
                if i == n//2 :
                    print(i, end = ' ')
                else :
                    print(i, "+", end = ' ')
        print()
    else :
        print("%d is NOT perfect." % n)