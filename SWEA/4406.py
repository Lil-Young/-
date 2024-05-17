# 모음이 보이지 않는 사람 / D3

T = int(input())
arr = ['a', 'e', 'i', 'o', 'u']
for tc in range(1, T+1):
    word = input()
    s = []
    for i in word:
        if i not in arr:
            s.append(i)
    print(f"#{tc} {''.join(s)}")
