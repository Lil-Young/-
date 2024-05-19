# String / D3

for tc in range(1, 11):
    T = int(input())
    target = input()
    s = input()
    limit = len(s)-len(target) + 1
    result = 0
    for i in range(limit):
        if s[i:i+len(target)] == target:
            result+=1
    print(f"#{tc} {result}")