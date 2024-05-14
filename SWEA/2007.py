# 패턴 마디의 길이 / D2

T = int(input())
for i in range(1, T+1):
    string = input()
    result = []
    for idx, s in enumerate(string):
        result.append(s)
        if ''.join(result) == string[idx+1:idx+1+len(result)]:
            print(f"#{i} {len(result)}")
            break