V = int(input())
a = list(map(str, input().rstrip()))
A = a.count("A"); B = a.count("B")
if A > B :
    print("A")
elif A < B :
    print("B")
else :
    print("Tie")